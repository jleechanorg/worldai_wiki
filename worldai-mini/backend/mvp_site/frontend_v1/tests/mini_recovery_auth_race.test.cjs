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
 let defer=false,fetches=0;
 const fetch=async()=>{fetches++;return {ok:true,json:()=>defer?new Promise(resolve=>{pending.push(resolve);}):Promise.resolve({sessions:[{session_id:'A',title:'private A'}]})};};
 vm.runInNewContext(source,{document:doc,firebase:{auth},window:{confirm:()=>true},fetch});ready();authCb(alice);
 return {els,alice,get fetches(){return fetches;},defer(){defer=true;},resolve(data,index=0){pending[index](data);},async waiting(count=1){while(pending.length<count)await tick();},switchTo(u){user=u;authCb(u);}};
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
