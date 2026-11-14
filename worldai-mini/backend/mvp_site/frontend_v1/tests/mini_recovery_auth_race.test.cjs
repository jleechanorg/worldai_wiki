const {test}=require('node:test');
const assert=require('node:assert/strict');
const vm=require('node:vm');
const fs=require('node:fs');
const path=require('node:path');
const source=fs.readFileSync(path.join(__dirname,'../mini-recovery.js'),'utf8');
const tick=()=>new Promise(setImmediate);
function setup(){
 const els=new Map();
 const el=()=>({hidden:true,textContent:'',children:[],value:'',checked:false,replaceChildren(){this.children=[];},append(...xs){this.children.push(...xs);}});
 let ready,authCb; const pending=[];
 const alice={uid:'alice',emailVerified:true,email:'a@test.invalid',getIdToken:async()=> 'token'};
 let user=alice;
 const auth=()=>({currentUser:user,onAuthStateChanged(cb){authCb=cb;},signOut:async()=>{user=null;authCb(null);}});
 const doc={addEventListener(_,cb){ready=cb;},getElementById(id){if(!els.has(id))els.set(id,el());return els.get(id);},createElement:el};
 let defer=false,fetches=0;const requests=[],responses=[];
 const fetch=async(url,options)=>{fetches++;requests.push({url,body:JSON.parse(options.body)});const response=responses.shift();if(response)return {ok:response.status<400,status:response.status,json:async()=>response.body};return {ok:true,json:()=>defer?new Promise((resolve,reject)=>{pending.push({resolve,reject});}):Promise.resolve({sessions:[{session_id:'A',title:'private A'}]})};};
 vm.runInNewContext(source,{document:doc,firebase:{auth},window:{confirm:()=>true},fetch});ready();authCb(alice);
 return {els,alice,requests,get fetches(){return fetches;},queue(response){responses.push(response);},defer(){defer=true;},resolve(data,index=0){pending[index].resolve(data);},reject(index=0){pending[index].reject(new Error('lost response'));},async waiting(count=1){while(pending.length<count)await tick();},switchTo(u){user=u;authCb(u);}};
}
for(const action of ['list','recover','link','remove'])for(const churn of ['bob','signout','alice-again'])test(`${action}: reject post-JSON ${churn} auth churn`,async()=>{
 const s=setup();
 if(action==='recover')await s.els.get('refresh').onclick();
 s.defer();let task;
 if(action==='recover')task=s.els.get('campaigns').children[0].children[1].onclick();
 else if(action==='list')task=s.els.get('refresh').onclick();
 else if(action==='link'){s.els.get('capability').value='PRIVATE';task=s.els.get('link').onsubmit({preventDefault(){}});}
 else task=s.els.get('remove').onclick();
 await s.waiting();
 s.switchTo(churn==='signout'?null:{uid:'bob',emailVerified:true,email:'b@test.invalid'});
 if(churn==='alice-again')s.switchTo(s.alice);
 const after=s.fetches;
 s.resolve({sessions:[{session_id:'A',title:'LEAK'}],session_key:'PRIVATE_BEARER',revision:7});await task;
 assert.equal(s.els.get('result').hidden,true);assert.equal(s.els.get('result').textContent,'');assert.equal(s.els.get('campaigns').children.length,0);assert.equal(s.els.get('status').textContent,'');assert.equal(s.fetches,after,'stale link must not fetch list');
});
test('newer request supersedes older body parse without auth change',async()=>{
 const s=setup();s.defer();const older=s.els.get('refresh').onclick();await s.waiting();
 const newer=s.els.get('remove').onclick();await s.waiting(2);s.resolve({},1);await newer;
 s.resolve({sessions:[{session_id:'old',title:'STALE'}]},0);await older;
 assert.equal(s.els.get('campaigns').children.length,0);
 assert.match(s.els.get('status').textContent,/removed/);
 void older;
});
test('a recovery button remains usable after a completed recovery',async()=>{
 const s=setup();await s.els.get('refresh').onclick();
 const button=s.els.get('campaigns').children[0].children[1];
 s.queue({status:200,body:{session_key:'FIRST_SYNTHETIC_KEY',revision:7}});
 await button.onclick();assert.equal(s.els.get('result').hidden,false);assert.match(s.els.get('result').textContent,/FIRST_SYNTHETIC_KEY/);
 const after=s.fetches;s.queue({status:200,body:{session_key:'SECOND_SYNTHETIC_KEY',revision:7}});await button.onclick();
 assert.equal(s.fetches,after+1,'a fresh confirmed action must not be blocked by an old request generation');
 assert.match(s.els.get('result').textContent,/SECOND_SYNTHETIC_KEY/);
});
test('refresh cannot supersede an in-flight recovery',async()=>{
 const s=setup();await s.els.get('refresh').onclick();
 const button=s.els.get('campaigns').children[0].children[1];s.defer();
 const recovery=button.onclick();await s.waiting();const afterStart=s.fetches;
 await s.els.get('refresh').onclick();assert.equal(s.fetches,afterStart);
 s.resolve({session_key:'PRIVATE_BEARER',revision:7},0);await recovery;
 assert.equal(button.disabled,false,'button is re-enabled after recovery');
 assert.equal(s.els.get('result').hidden,false);
});
test('recovery cannot be superseded by removing recovery links',async()=>{
 const s=setup();await s.els.get('refresh').onclick();
 const button=s.els.get('campaigns').children[0].children[1];s.defer();
 const recovery=button.onclick();await s.waiting();const afterStart=s.fetches;
 const removal=s.els.get('remove').onclick();await tick();
 const removalStarted=s.fetches>afterStart;
 s.resolve({session_key:'NEW_SYNTHETIC_KEY',revision:7},0);
 if(removalStarted){await s.waiting(2);s.resolve({},1);}await removal;await recovery;
 assert.equal(removalStarted,false,'removal must not start during recovery');
 assert.equal(s.els.get('result').hidden,false);
 assert.match(s.els.get('result').textContent,/NEW_SYNTHETIC_KEY/);
});
test('recovery cannot start while link removal is in flight',async()=>{
 const s=setup();await s.els.get('refresh').onclick();
 const button=s.els.get('campaigns').children[0].children[1];s.defer();
 const removal=s.els.get('remove').onclick();await s.waiting();const afterStart=s.fetches;
 const recovery=button.onclick();await tick();const recoveryStarted=s.fetches>afterStart;
 s.resolve({},0);if(recoveryStarted){await s.waiting(2);s.resolve({session_key:'NEW_SYNTHETIC_KEY',revision:7},1);}
 await removal;await recovery;
 assert.equal(recoveryStarted,false,'recovery must not start during removal');
});
test('signout immediately clears private output while removal is pending',async()=>{
 const s=setup();s.els.get('result').hidden=false;s.els.get('result').textContent='PRIVATE_TEST_CAPABILITY';s.defer();
 const removal=s.els.get('remove').onclick();await s.waiting();
 await s.els.get('signout').onclick();
 const wasCleared=s.els.get('result').hidden && s.els.get('result').textContent==='';
 s.resolve({},0);await removal;
 assert.equal(wasCleared,true,'signout must immediately clear private output');
});
test('a lost recovery response warns against unlinking',async()=>{
 const s=setup();await s.els.get('refresh').onclick();const button=s.els.get('campaigns').children[0].children[1];s.defer();
 const recovery=button.onclick();await s.waiting();s.reject();await recovery;
 assert.match(s.els.get('status').textContent,/outcome is unknown/i);assert.equal(s.els.get('result').hidden,true);
});
test('confirming a saved recovered capability sends it through the verified link action',async()=>{
 const s=setup();await s.els.get('refresh').onclick();const button=s.els.get('campaigns').children[0].children[1];s.defer();
 const recovery=button.onclick();await s.waiting();s.resolve({session_key:'NEW_SYNTHETIC_KEY',revision:7});await recovery;
 const saved=s.els.get('result').children[0];const confirmation=saved.onclick();await s.waiting(2);
 assert.equal(s.requests.at(-1).url,'/api/mini-recovery/link');
 assert.equal(JSON.stringify(s.requests.at(-1).body),JSON.stringify({session_key:'NEW_SYNTHETIC_KEY',consent:true}));
 s.resolve({linked:true},1);await confirmation;assert.equal(saved.disabled,true);
});
test('unconfirmed removal requires a distinct explicit discard action',async()=>{
 const s=setup();s.queue({status:409,body:{error:'RECOVERY_CONFIRMATION_REQUIRED'}});
 await s.els.get('remove').onclick();assert.equal(JSON.stringify(s.requests[0].body),'{}');
 const force=s.els.get('status').children[0];assert.match(force.textContent,/accept possible access loss/i);
 s.queue({status:200,body:{removed:true}});await force.onclick();
 assert.equal(JSON.stringify(s.requests[1].body),JSON.stringify({discard_unconfirmed:true}));
});
test('signout during recovery redacts a late capability',async()=>{
 const s=setup();await s.els.get('refresh').onclick();const button=s.els.get('campaigns').children[0].children[1];s.defer();
 const recovery=button.onclick();await s.waiting();await s.els.get('signout').onclick();
 s.resolve({session_key:'LATE_PRIVATE_CAPABILITY',revision:7});await recovery;
 assert.equal(s.els.get('result').hidden,true);assert.equal(s.els.get('result').textContent,'');
});
