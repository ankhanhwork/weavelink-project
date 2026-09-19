import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

// Documentation integrity only: this does not execute the future application.
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..');
const errors = [];
let checks = 0;
const check = (condition, message) => { checks++; if (!condition) errors.push(message); };
const read = relative => fs.readFileSync(path.join(root, relative), 'utf8').replace(/^\uFEFF/, '');
const files = [];
function walk(dir) {
  for (const entry of fs.readdirSync(path.join(root, dir), { withFileTypes: true })) {
    const relative = path.posix.join(dir, entry.name);
    if (entry.isDirectory()) walk(relative);
    else if (entry.name.endsWith('.md')) files.push(relative);
  }
}
for (const dir of ['docs', 'specs', 'screens']) walk(dir);
files.push('README.md');
const texts = new Map(files.map(f => [f, read(f)]));
const catalogue = read('docs/function-list.md');
const functionKeys = [...catalogue.matchAll(/^\| \d+ \| UC-[A-Z]\d+ \| (MFG-\d+\/F-[A-Z]+-\d+) \|/gm)].map(m => m[1]);
const knownFunctions = new Set(functionKeys);
check(functionKeys.length === 94, `Expected 94 catalogue functions, got ${functionKeys.length}`);
check(knownFunctions.size === 94, 'Duplicate module-qualified function keys');
const expected = [['USER',11],['PROF',5],['ACC',8],['PROD',11],['DES',11],['PAY',6],['ORD',7],['ORD',8],['CONTR',9],['MER',7],['DA',3],['SYS',8]];
const useCases = [...read('docs/architecture/use-case.md').matchAll(/^\| (UC-[A-Z]\d+) \|/gm)].map(m => m[1]);
const knownUC = new Set(useCases);
check(useCases.length === 49 && knownUC.size === 49, 'Expected 49 unique use-case rows');
for (const [i, [prefix, count]] of expected.entries()) {
  const mod = `MFG-${String(i+1).padStart(2,'0')}`;
  const specPath = `specs/spec-${mod}.md`;
  const spec = texts.get(specPath) || '';
  check(!!spec, `${mod}: specification missing`);
  const seen = new Set([...spec.matchAll(/\b(F-[A-Z]+-\d{3})\b/g)].map(m=>m[1]));
  for (let n=1;n<=count;n++) {
    const f = `F-${prefix}-${String(n).padStart(3,'0')}`;
    check(knownFunctions.has(`${mod}/${f}`), `${mod}/${f}: missing catalogue row`);
    check(seen.has(f), `${mod}/${f}: missing spec contract`);
    check(spec.includes(`FR-${String(n).padStart(3,'0')}`), `${mod}: missing FR-${n}`);
  }
  for (const line of catalogue.split('\n').filter(l=>l.includes(`| ${mod}/F-`))) {
    const uc = line.match(/UC-[A-Z]\d+/)?.[0];
    check(spec.includes(uc), `${mod}: missing owned use-case reference ${uc}`);
  }
  check(spec.includes('system-decisions.md'), `${mod}: missing common contract link`);
  check(spec.includes('user-input-needed.md'), `${mod}: missing human-input register link`);
}
const screenFiles = files.filter(f => /^screens\/S\d{2}-.*\.md$/.test(f));
check(screenFiles.length === 43, `Expected 43 screens, got ${screenFiles.length}`);
const screenCatalogue = read('docs/screen-list.md');
const listedScreens = [...screenCatalogue.matchAll(/^\| (S\d{2}) \|/gm)].map(m=>m[1]);
check(listedScreens.length === 43 && new Set(listedScreens).size === 43, 'Expected 43 unique screen catalogue rows');
for (let i=1;i<=43;i++) {
  const id=`S${String(i).padStart(2,'0')}`;
  const matches=screenFiles.filter(f=>path.basename(f).startsWith(id+'-'));
  check(matches.length===1, `${id}: must have exactly one detailed file`);
  check(listedScreens.includes(id), `${id}: missing screen index row`);
  if (matches.length!==1) continue;
  const f=matches[0], body=texts.get(f);
  check(screenCatalogue.includes(`../${f}`), `${id}: missing clickable index link`);
  check(body.includes('system-decisions.md'), `${id}: missing shared decision link`);
  check(/\.\.\/specs\/spec-MFG-\d+\.md/.test(body), `${id}: missing module link`);
  for (const heading of ['Fields and validation','Actions and navigation','States','Acceptance scenarios'])
    check(body.includes(heading),`${id}: missing ${heading}`);
  check(!body.includes('| Screen action |'), `${id}: generic action placeholder must be replaced`);
  const functionsLine=body.split('\n').find(line=>line.startsWith('Functions:'))||'';
  check(!/(?<!\/)\bF-[A-Z]+-\d{3}\b/.test(functionsLine),`${id}: cross-document function references must be module-qualified`);
}
const screenById = id => texts.get(screenFiles.find(f=>path.basename(f).startsWith(id+'-'))) || '';
const screenRules = {
  S03: ['Accept invitation','Company Admin','Sales Consultant','System Admin'],
  S09: ['MFG-04/F-PROD-002','Customer capability'],
  S16: ['AwaitingPayment','Paid','Assigned','InProgress','Delivered','committed_due_at','refund'],
  S26: ['MFG-07/F-ORD-001'],
  S28: ['Assigned Consultant'],
  S30: ['Publish','Archive','MFG-09/F-CONTR-006'],
  S31: ['Publish','MFG-09/F-CONTR-006'],
  S32: ['Archive','MFG-09/F-CONTR-006'],
  S36: ['MFG-06/F-PAY-005'],
  S39: ['daily_backup_time','daily_retention_count','weekly_retention_count','design_service_fee_vnd'],
  S41: ['Provisioning','tax_id','address','admin_contact_info','initial_admin_email']
};
for (const [id, required] of Object.entries(screenRules))
  for (const token of required) check(screenById(id).includes(token),`${id}: missing semantic contract ${token}`);
const forbiddenScreenText = {
  S09: ['MFG-04/F-PROD-003'],
  S17: ['MFG-05/F-DES-007'],
  S26: ['MFG-07/MFG-07','MFG-07/F-ORD-004'],
  S29: ['MFG-08/F-ORD-008'],
  S36: ['MFG-06/F-PAY-006','Export'],
  S38: ['MFG-01/F-USER-006']
};
for (const [id, forbidden] of Object.entries(forbiddenScreenText))
  for (const token of forbidden) check(!screenById(id).includes(token),`${id}: forbidden or incorrect mapping ${token}`);
let localLinks=0, diagrams=0;
for (const [file, body] of texts) {
  check(!/NEEDS CLARIFICATION|\bTBD\b|\bTODO\b|\[NEEDS/i.test(body), `${file}: unresolved placeholder`);
  check(!/UC-Cancellations\b/.test(body), `${file}: invented use-case ID`);
  const fences=body.match(/^\s*```/gm)||[];
  check(fences.length%2===0, `${file}: unbalanced code fences`);
  diagrams+=(body.match(/^```mermaid/gm)||[]).length;
  for (const match of body.matchAll(/!?\[[^\]\n]*\]\((<?[^\s)]+>?)\)/g)) {
    let target=match[1].replace(/^<|>$/g,'');
    if (/^(?:https?:|mailto:|tel:|data:|#)/.test(target)) continue;
    target=decodeURIComponent(target.split('#')[0]);
    const absolute=path.resolve(root,path.dirname(file),target);
    check(absolute.startsWith(root+path.sep), `${file}: local link escapes repository: ${target}`);
    check(fs.existsSync(absolute), `${file}: missing link target ${target}`);
    localLinks++;
  }
  for (const m of body.matchAll(/\b(MFG-\d{2}\/F-[A-Z]+-\d{3})\b/g))
    check(knownFunctions.has(m[1]), `${file}: unknown function key ${m[1]}`);
  for (const m of body.matchAll(/\b(UC-[A-Z]\d{2})\b/g))
    check(knownUC.has(m[1]), `${file}: unknown use-case ${m[1]}`);
  for (const m of body.matchAll(/\b(S\d{2})\b/g))
    check(listedScreens.includes(m[1]),`${file}: unknown screen ${m[1]}`);
  let columns=null;
  for (const [i,line] of body.split('\n').entries()) {
    if(line.startsWith('|')) {
      check(line.trimEnd().endsWith('|'),`${file}:${i+1}: unterminated table row`);
      const count=(line.match(/(?<!\\)\|/g)||[]).length-1;
      if(columns===null) columns=count;
      check(count===columns,`${file}:${i+1}: expected ${columns} table columns, got ${count}; escape literal pipes`);
    } else columns=null;
  }
}
const sequenceIds=[...read('docs/architecture/sequence.md').matchAll(/^## (SD-\d{2}[AB]?) /gm)].map(m=>m[1]);
check(sequenceIds.join(',')==='SD-01,SD-02,SD-03,SD-04,SD-05A,SD-05B,SD-06,SD-07,SD-08,SD-09','Legacy sequence ID set changed');
check(files.filter(f=>/user-input-needed\.md$/.test(f)).length===1,'Exactly one human input register required');
const png=fs.readdirSync(path.join(root,'screens/img')).filter(f=>f.endsWith('.png'));
check(png.length===17,'Expected original 17 PNG assets');
const priceRows = read('docs/acceptance-checklist.md').split('\n').filter(l=>/^\| (Standard|Merge|Rounding|Small subtotal) \|/.test(l));
check(priceRows.length===4,'Expected four worked price examples');
for(const row of priceRows) {
  const [name,qty,unit,surcharge,merge,shipping,subtotal,discount,total]=row.split('|').slice(1,-1).map(x=>x.trim());
  const calculatedSubtotal=BigInt(qty)*(BigInt(unit)+BigInt(surcharge));
  const calculatedDiscount=merge==='Yes'?calculatedSubtotal*5n/100n:0n;
  check(calculatedSubtotal===BigInt(subtotal),`${name}: subtotal example mismatch`);
  check(calculatedDiscount===BigInt(discount),`${name}: discount example mismatch`);
  check(calculatedSubtotal-calculatedDiscount+BigInt(shipping)===BigInt(total),`${name}: total example mismatch`);
}
const report={passed:errors.length===0,checks,markdownFiles:files.length,functions:functionKeys.length,useCases:useCases.length,screens:screenFiles.length,localLinks,mermaidBlocks:diagrams,errors};
if (process.argv.includes('--build')) {
  fs.mkdirSync(path.join(root,'tmp'),{recursive:true});
  fs.writeFileSync(path.join(root,'tmp','documentation-index.json'),JSON.stringify({...report,files,functionKeys,useCases,screenIds:listedScreens},null,2)+'\n');
}
console.log(JSON.stringify(report,null,2));
process.exitCode=errors.length ? 1 : 0;
