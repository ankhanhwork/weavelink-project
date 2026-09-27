import test from 'node:test';
import assert from 'node:assert/strict';
import {samplePrint,rasterPrint,inkLight} from '../web/print-surface.js';
test('transparent edge retains ink hue instead of a dark fringe',()=>{
  const edge=samplePrint(new Uint8ClampedArray([255,80,20,255,0,0,0,0]),2,1,.5,0);
  assert.deepEqual(edge,[255,80,20,127.5]);
});
test('shared triangle edge has neither an alpha hole nor doubled opacity',()=>{
  const source=new Uint8ClampedArray(4*4*4);for(let p=0;p<source.length;p+=4)source.set([250,100,50,128],p);
  const points=[[0,0],[16,0],[16,16],[0,16]],uv=[[0,0],[4,0],[4,4],[0,4]];
  const triangles=[[0,1,2],[0,2,3]].map(ids=>({source:ids.map(i=>uv[i]),target:ids.map(i=>points[i])}));
  const out=rasterPrint(source,4,4,16,16,triangles);
  for(let p=0;p<out.length;p+=4)assert.deepEqual([...out.slice(p,p+4)],[250,100,50,128]);
});
test('blank regions remain transparent outside projected print area',()=>{
  const out=rasterPrint(new Uint8ClampedArray([255,0,0,255]),1,1,4,4,[{source:[[0,0],[1,0],[0,1]],target:[[1,1],[3,1],[1,3]]}]);
  assert.equal(out[3],0);assert.equal(out[(1*4+1)*4+3],255);assert.equal(out[(3*4+3)*4+3],0);
});
test('ink follows garment light and retains texture contrast',()=>{
  assert.ok(inkLight(150,150)<inkLight(235,235));
  assert.ok(inkLight(200,220)<inkLight(200,180));
});
