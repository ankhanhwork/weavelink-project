import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

// Documentation integrity only; this repository has no application runtime.
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const errors = [];
let checks = 0;
const check = (condition, message) => { checks++; if (!condition) errors.push(message); };
const read = relative => fs.readFileSync(path.join(root, relative), 'utf8').replace(/^\uFEFF/, '');
const files = [];
function walk(relative) {
  const absolute = path.join(root, relative);
  if (!fs.existsSync(absolute)) return;
  for (const entry of fs.readdirSync(absolute, { withFileTypes: true })) {
    const child = path.posix.join(relative, entry.name);
    if (entry.isDirectory()) walk(child);
    else if (entry.name.endsWith('.md')) files.push(child);
  }
}
for (const dir of ['docs', 'specs', 'screens', 'ai-files/docs']) walk(dir);
files.push('README.md');
const texts = new Map(files.map(file => [file, read(file)]));

const functionCatalogue = read('docs/function-list.md');
const functionKeys = [];
let activeModule = null;
for (const line of functionCatalogue.split('\n')) {
  const moduleMatch = line.match(/^## [IVX]+\. (MFG-\d{2}):/);
  if (moduleMatch) activeModule = moduleMatch[1];
  const functionMatch = line.match(/^\| \d+ \| UC-[A-Z]\d{2} \|[^|]*\| (F-[A-Z]+-\d{3}) \|/);
  if (functionMatch && activeModule) functionKeys.push(`${activeModule}/${functionMatch[1]}`);
}
const knownFunctions = new Set(functionKeys);
check(functionKeys.length === 96, `Expected 96 function rows, got ${functionKeys.length}`);
check(knownFunctions.size === 96, 'Function keys must be unique after module qualification');
const detailedFunctionRows = functionCatalogue.split('\n').filter(line => /^\| \d+ \| UC-[A-Z]\d{2} \|/.test(line));
for (const line of detailedFunctionRows) {
  const cells = line.slice(1, -1).split('|').map(cell => cell.trim());
  check(cells.length === 11, `Function-list row must have 11 columns: ${line}`);
  check(Boolean(cells[5]) && !/validated contract|defined in MFG-/i.test(cells[5]), `${cells[3]}: Function overview is not fully populated`);
  check(Boolean(cells[8]) && !/Typed request fields|defined in MFG-/i.test(cells[8]), `${cells[3]}: Input is not fully populated`);
  check(Boolean(cells[9]) && !/Typed result|defined in MFG-/i.test(cells[9]), `${cells[3]}: Output is not fully populated`);
}

const useCases = [...read('docs/architecture/use-case.md').matchAll(/^\| (UC-[A-Z]\d{2}) \|/gm)].map(match => match[1]);
const knownUseCases = new Set(useCases);
check(useCases.length === 49 && knownUseCases.size === 49, `Expected 49 unique use cases, got ${useCases.length}`);

const expectedFunctions = [['USER',11],['PROF',5],['ACC',8],['PROD',11],['DES',13],['PAY',6],['ORD',7],['ORD',8],['CONTR',9],['MER',7],['DA',3],['SYS',8]];
const requiredSpecHeadings = [
  '## 1. Purpose and scope (mandatory)', '## 2. Actors (mandatory)',
  '## 3. User scenarios and acceptance criteria (mandatory)', '## 4. Flows (mandatory)',
  '### 4.1 Usage flow', '### 4.2 Sequence for the main flow',
  '## 5. Functional requirements (mandatory)', '### 5.1 Input / Output contract',
  '### 5.2 Business rules', '## 6. Key entities (mandatory)', '## 7. Screens involved',
  '## 8. Success criteria (mandatory)', '## 9. Assumptions', '## 10. Open questions',
  '## 11. Traceability to DBIZ2', '## Completion checklist'
];
const requiredSpecTables = [
  '| Actor | Role in this module | Where it comes from |',
  '| FR ID | DBIZ2 Subfunction ID | Requirement (system MUST ...) | Actor | Priority |',
  '| FR ID | Input field | Type | Required | Output field | Type | Notes / validation |',
  '| Rule ID | Rule | Why it exists |',
  '| Entity | Attributes (from Input/Output fields) | Relationships |',
  '| Screen ID | Screen name | Priority | Screen Spec file |',
  '| SC ID | Criterion | How it is measured |',
  '| # | Question | Blocking? | Owner | Status |',
  '| Spec section | DBIZ2 source | Location |'
];
for (const [index, [prefix, count]] of expectedFunctions.entries()) {
  const module = `MFG-${String(index + 1).padStart(2, '0')}`;
  const file = `specs/spec-${module}.md`;
  const body = texts.get(file) || '';
  check(body.startsWith('# Spec Document:'), `${file}: teacher-format title missing`);
  for (const heading of requiredSpecHeadings) check(body.includes(heading), `${file}: missing ${heading}`);
  for (const header of requiredSpecTables) check(body.includes(header), `${file}: missing teacher-format table ${header}`);
  const questionSection = body.match(/## 10\. Open questions([\s\S]*?)## 11\./)?.[1] || '';
  check(/No remaining open questions|Resolved/.test(questionSection), `${file}: open-question section is not explicitly resolved`);
  for (let number = 1; number <= count; number++) {
    const functionId = `F-${prefix}-${String(number).padStart(3, '0')}`;
    const requirementId = `FR-${String(number).padStart(3, '0')}`;
    check(knownFunctions.has(`${module}/${functionId}`), `${module}/${functionId}: missing function-list row`);
    check(body.includes(functionId), `${file}: missing ${functionId}`);
    check(body.includes(requirementId), `${file}: missing ${requirementId}`);
  }
}

const screenFiles = files.filter(file => /^screens\/S\d{2}-.*\.md$/.test(file));
const screenCatalogue = read('docs/screen-list.md');
const listedScreens = [...screenCatalogue.matchAll(/^\| (S\d{2}) \|/gm)].map(match => match[1]);
check(screenFiles.length === 45, `Expected 45 screen specs, got ${screenFiles.length}`);
check(listedScreens.length === 45 && new Set(listedScreens).size === 45, 'Expected 45 unique screen-list rows');
const inheritedWithMockups = new Set(['S01','S02','S03','S06','S08','S09','S13','S15','S17','S22','S23','S25','S26','S27','S34','S35']);
const requiredScreenHeadings = ['## 1. Purpose','## 2. Mockup','## 3. Element inventory','## 4. States','## 5. Interactions and navigation','## 6. Screen-level rules','## 7. Linked requirements','## 8. Responsive and accessibility notes','## 9. Open questions','## Completion checklist'];
const requiredScreenTables = [
  '| Field | Value |',
  '| # | Element | Type | Content / data source | Required | Validation |',
  '| State | What the user sees | Trigger |',
  '| # | Element | User action | System response | Goes to screen |',
  '| Rule ID | Rule | Source |',
  '| # | Question | Blocking? | Status |'
];
for (let number = 1; number <= 46; number++) {
  if (number === 16) continue;
  const id = `S${String(number).padStart(2, '0')}`;
  const matches = screenFiles.filter(file => path.basename(file).startsWith(`${id}-`));
  check(matches.length === 1, `${id}: expected exactly one screen spec`);
  check(listedScreens.includes(id), `${id}: missing screen-list row`);
  if (matches.length !== 1) continue;
  const body = texts.get(matches[0]);
  check(body.startsWith(`# Screen Spec: ${id} `), `${matches[0]}: teacher-format title missing`);
  for (const heading of requiredScreenHeadings) check(body.includes(heading), `${matches[0]}: missing ${heading}`);
  for (const header of requiredScreenTables) check(body.includes(header), `${matches[0]}: missing teacher-format table ${header}`);
  const questionSection = body.match(/## 9\. Open questions([\s\S]*?)## Completion checklist/)?.[1] || '';
  check(/No remaining open questions|Resolved/.test(questionSection), `${matches[0]}: open-question section is not explicitly resolved`);
  const mockupRef = body.match(/^\| Mockup image \| `?img\/([^ |`]+\.png)`? \|$/m)?.[1];
  if (mockupRef) {
    check(fs.existsSync(path.join(root, 'screens', 'img', mockupRef)), `${matches[0]}: mockup image file missing`);
    check(body.includes(`![`) && body.includes(`img/${mockupRef}`), `${matches[0]}: mockup image not embedded in section 2`);
    check(!body.includes("Don't have mockup"), `${matches[0]}: linked screen incorrectly marked without mockup`);
  } else {
    check((body.match(/Don't have mockup/g) || []).length >= 2, `${matches[0]}: exact no-mockup note must appear in metadata and section 2`);
  }
  check(screenCatalogue.includes(`../${matches[0]}`), `${id}: screen-list link missing`);
}

check(read('README.md').includes('## MVP Scope'), 'README: MVP Scope missing');
const readme = read('README.md');
const mergeSpec = read('specs/spec-MFG-10.md');
const s35 = read('screens/S35-order_payment_screen.md');
const s39 = read('screens/S39-system_configuration_and_backup_restore_screen.md');
const acceptance = read('ai-files/docs/acceptance-checklist.md');
check(readme.includes('one `Sales Admin` for order/sample/contract operations') && readme.includes('one `Sales` identity') && readme.includes('one `System Admin` bootstrap identity') && readme.includes('one verified Customer test account'), 'README: MVP seed identities must name operational and bootstrap roles');
check(/\*\*MVP implementation slice:\*\*[\s\S]*fixed Dony template[\s\S]*Sales Admin manually/.test(readme), 'README: MVP vertical slice must include minimum contract and fulfillment steps');
check(mergeSpec.includes('canonical source for MFG-10 policy numbers and formulas') && mergeSpec.includes('840,000 VND') && mergeSpec.includes('2,800,000 VND') && mergeSpec.includes('seven calendar days'), 'MFG-10: canonical v3 policy values missing');
check(s35.includes('min(subtotal_vnd, 840000)') && !/5\s*\/\s*100|5%/.test(s35), 'S35: merge discount must match the MFG-10 v3 capped-amount formula');
check(s39.includes('min(order_subtotal_vnd, 840000)') && !/merge_discount_percent|Fixed at 5/.test(s39), 'S39: displayed merge policy must match MFG-10 v3');
check(acceptance.includes('Worked price-policy v3 examples') && !acceptance.includes('price-policy v1'), 'Acceptance checklist: pricing examples must use policy v3');
check(!/another-company staff|company with open work is deleted/i.test(acceptance), 'Acceptance checklist: obsolete multi-tenant scenarios remain');
check(readme.includes('45 active screen IDs (`S01`–`S15` and `S17`–`S46`; S16 is retired)'), 'README: active screen range must match the catalogue');
const mfg06 = read('specs/spec-MFG-06.md');
const screenList = read('docs/screen-list.md');
const mfg04 = read('specs/spec-MFG-04.md');
const userInput = read('ai-files/docs/user-input-needed.md');
check(mfg06.includes('`merge_opt_in=false`') && mfg06.includes('`merge_discount_vnd=0`') && mfg06.includes('Do not render merge choices or discounts in MVP checkout'), 'MFG-06: MVP must explicitly disable merge selection and discounts');
check(mfg06.includes('dormant post-MVP MFG-10 v3 branch') && mfg06.includes('post-MVP only: merge choice/version'), 'MFG-06: Must quote requirements must distinguish MVP from post-MVP merge');
check(/^\| ID \| Screen name \| Screen Overview \| MVP \|$/m.test(screenList), 'screen-list: MVP scope column missing');
const mvpScreenRows = [...screenList.matchAll(/^\| (S\d{2}) \|[^\n]*\| (Yes(?: —[^|]*)?|No(?: —[^|]*)?) \|$/gm)].map(match => [match[1], match[2]]);
check(mvpScreenRows.length === 45 && new Set(mvpScreenRows.map(row => row[0])).size === 45, `screen-list: expected 45 unique rows with explicit MVP scope, got ${mvpScreenRows.length}`);
for (const id of ['S04','S05','S17','S29','S33','S34','S44','S45','S46']) check(mvpScreenRows.some(([screen, scope]) => screen === id && scope.startsWith('Yes')), `${id}: required MVP screen must be marked Yes`);
for (const id of ['S23','S24','S30','S31','S32','S39','S40','S41','S42']) check(mvpScreenRows.some(([screen, scope]) => screen === id && scope.startsWith('No')), `${id}: deferred screen must be marked No`);
check(/seed at least one complete, Published Dony product base/i.test(readme) && /pre-seed at least one complete Published Dony product base/i.test(mfg04), 'MVP: product catalog seed data and product-rule readiness must be explicit');
check(/self-design is Must|Self-design\/save is Must/.test(userInput) && !/single internal admin login is sufficient/i.test(userInput), 'user-input-needed: duplicate MVP scope must not retain superseded priorities or seed assumptions');
check(!/policy-v1|policy v1|read-only in v1/i.test(texts.get('specs/spec-MFG-12.md') + texts.get('docs/function-list.md') + texts.get('screens/S39-system_configuration_and_backup_restore_screen.md')), 'MFG-10 settings references must not retain stale policy-v1 labels');
check(read('README.md').includes('## Open clarification areas'), 'README: original clarification-area section missing');
check(/^\| ID \| Screen name \| Screen Overview \| MVP \|/m.test(screenCatalogue), 'screen-list: MVP scope table header missing');
check(/^# Function List$/m.test(functionCatalogue), 'function-list: original title missing');
check(/^\| No \| Use Case ID \| Function name \| Subfunction ID \| Subfunction name \| Function overview \| Category \| Actor \| Input \| Output \| Priority \|/m.test(functionCatalogue), 'function-list: original eleven-column schema missing');
check(/^\| Use Case ID \| Use case \| Primary actor \| Other actors \| Subfunctions \|/m.test(read('docs/architecture/use-case.md')), 'use-case: original five-column schema missing');

const sequenceIds = [...read('docs/architecture/sequence.md').matchAll(/^# .*?— (SD-\d{2}[AB]?):/gm)].map(match => match[1]);
check(sequenceIds.join(',') === 'SD-01,SD-02,SD-03,SD-04,SD-05A,SD-05B,SD-06,SD-07,SD-08,SD-09', 'Sequence heading format or ID set changed');

const originalAreas = ['README.md', ...files.filter(file => /^(docs|specs|screens)\//.test(file))];
for (const file of originalAreas) check(!texts.get(file).includes('ai-files'), `${file}: original documentation must not depend on ai-files`);

let localLinks = 0;
let mermaidBlocks = 0;
for (const [file, body] of texts) {
  check(!/NEEDS CLARIFICATION|\bTBD\b|\bTODO\b|\[NEEDS/i.test(body), `${file}: unresolved placeholder`);
  check(!/\|\s*(?:Unresolved|Pending decision|Awaiting answer)\s*\|/i.test(body), `${file}: unresolved decision status`);
  const fences = body.match(/^\s*```/gm) || [];
  check(fences.length % 2 === 0, `${file}: unbalanced code fences`);
  mermaidBlocks += (body.match(/^```mermaid/gm) || []).length;
  for (const match of body.matchAll(/!?\[[^\]\n]*\]\((<?[^\s)]+>?)\)/g)) {
    let target = match[1].replace(/^<|>$/g, '');
    if (/^(?:https?:|mailto:|tel:|data:|#)/.test(target)) continue;
    target = decodeURIComponent(target.split('#')[0]);
    const absolute = path.resolve(root, path.dirname(file), target);
    check(absolute.startsWith(root + path.sep), `${file}: link escapes repository: ${target}`);
    check(fs.existsSync(absolute), `${file}: missing link target ${target}`);
    localLinks++;
  }
  for (const match of body.matchAll(/\b(MFG-\d{2}\/F-[A-Z]+-\d{3})\b/g)) check(knownFunctions.has(match[1]), `${file}: unknown function key ${match[1]}`);
  for (const match of body.matchAll(/\b(UC-[A-Z]\d{2})\b/g)) check(knownUseCases.has(match[1]), `${file}: unknown use case ${match[1]}`);
  let columns = null;
  for (const [lineIndex, line] of body.split('\n').entries()) {
    if (line.startsWith('|')) {
      check(line.trimEnd().endsWith('|'), `${file}:${lineIndex + 1}: unterminated table row`);
      const count = (line.match(/(?<!\\)\|/g) || []).length - 1;
      if (columns === null) columns = count;
      check(count === columns, `${file}:${lineIndex + 1}: expected ${columns} table columns, got ${count}`);
    } else columns = null;
  }
}

const pngs = fs.readdirSync(path.join(root, 'screens', 'img')).filter(file => file.endsWith('.png'));
const referencedPngs = screenFiles.filter(file => texts.get(file).match(/^\| Mockup image \| `?img\/([^ |`]+\.png)`? \|$/m)).length;
check(pngs.length === referencedPngs, `Every PNG must be linked from one screen spec (${pngs.length} files, ${referencedPngs} referenced)`);
check(fs.existsSync(path.join(root, 'ai-files', 'docs', 'user-input-needed.md')), 'Preserved user input register missing from ai-files');
check(!fs.existsSync(path.join(root, 'docs', 'user-input-needed.md')), 'AI-created user input register must not remain under docs');

const report = { passed: errors.length === 0, checks, markdownFiles: files.length, functions: functionKeys.length, useCases: useCases.length, screens: screenFiles.length, localLinks, mermaidBlocks, errors };
if (process.argv.includes('--build')) {
  const output = path.join(root, 'ai-files', 'tmp', 'documentation-index.json');
  fs.mkdirSync(path.dirname(output), { recursive: true });
  fs.writeFileSync(output, `${JSON.stringify({ ...report, files, functionKeys, useCases, screenIds: listedScreens }, null, 2)}\n`);
}
console.log(JSON.stringify(report, null, 2));
process.exitCode = errors.length ? 1 : 0;
