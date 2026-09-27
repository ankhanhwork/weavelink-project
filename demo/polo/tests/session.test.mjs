import test from 'node:test';
import assert from 'node:assert/strict';
import {acceptsTryOn} from '../web/session-guard.js';

const captured={session:3,person:5,revision:7,job:9};

test('an unchanged request accepts its matching server revision',()=>{
  assert.equal(acceptsTryOn(captured,{...captured},7),true);
});
for(const [name,current,revision] of [
  ['design edited while decoding result',{...captured,revision:8},7],
  ['photo replaced while request is pending',{...captured,person:6},7],
  ['session ended and design revision reused',{session:4,person:5,revision:7,job:9},7],
  ['new generation started for same design',{...captured,job:10},7],
  ['server returns another design',{...captured},6],
  ['server omits design revision',{...captured},undefined],
]) {
  test(`late reply discarded: ${name}`,async()=>{
    let installed=null;
    const reply=await Promise.resolve({designRevision:revision,image:'old-result'});
    if(acceptsTryOn(captured,current,reply.designRevision))installed=reply.image;
    assert.equal(installed,null);
  });
}
