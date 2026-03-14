/**
 * Frontend Testlari - HTML, CSS, JavaScript
 * Jami: 50 ta test
 * Brauzerda ishga tushirish uchun
 */

// Test natijalari
const testResults = {
    passed: 0,
    failed: 0,
    tests: []
};

// Test yordamchi funksiyasi
function test(name, fn) {
    try {
        fn();
        testResults.passed++;
        testResults.tests.push({ name: name, status: 'PASSED' });
        console.log(`✓ ${name}`);
    } catch (e) {
        testResults.failed++;
        testResults.tests.push({ name: name, status: 'FAILED', error: e.message });
        console.error(`✗ ${name}: ${e.message}`);
    }
}

// ============================================================================
// 1. HTML TESTLARI (1-20)
// ============================================================================

console.log('=== HTML TESTLARI ===');

test('HTML: Hujjat tuzilmasini tekshirish', () => {
    const html = '<!DOCTYPE html><html><head><title>Test</title></head><body></body></html>';
    if (!html.includes('<!DOCTYPE html>')) throw new Error('DOCTYPE topilmadi');
    if (!html.includes('<html>')) throw new Error('html tegi topilmadi');
});

test('HTML: Sarlavha teglari mavjud', () => {
    const headings = ['<h1>', '<h2>', '<h3>', '<h4>', '<h5>', '<h6>'];
    headings.forEach(tag => {
        if (!`<h1></h1>`.includes(tag)) throw new Error(`${tag} topilmadi`);
    });
});

test('HTML: P tegi', () => {
    const p = '<p>Matn</p>';
    if (!p.includes('<p>') || !p.includes('</p>')) throw new Error('p tegi xato');
});

test('HTML: A (link) tegi', () => {
    const a = '<a href="url">Link</a>';
    if (!a.includes('href=')) throw new Error('href atributi topilmadi');
});

test('HTML: Img tegi', () => {
    const img = '<img src="rasm.jpg" alt="Rasm">';
    if (!img.includes('src=') || !img.includes('alt=')) throw new Error('img atributlari xato');
});

test('HTML: Ul/OL royxatlari', () => {
    const ul = '<ul><li>Element</li></ul>';
    const ol = '<ol><li>Element</li></ol>';
    if (!ul.includes('<ul>') || !ol.includes('<ol>')) throw new Error('Ro\'yxat teglari xato');
});

test('HTML: Jadval teglari', () => {
    const table = '<table><tr><td>Ma\'lumot</td></tr></table>';
    if (!table.includes('<table>') || !table.includes('<tr>') || !table.includes('<td>')) {
        throw new Error('Jadval teglari topilmadi');
    }
});

test('HTML: Forma teglari', () => {
    const form = '<form action="/submit" method="POST"><input type="text"></form>';
    if (!form.includes('<form>') || !form.includes('method=') || !form.includes('<input>')) {
        throw new Error('Forma elementlari topilmadi');
    }
});

test('HTML: Button tegi', () => {
    const btn = '<button type="submit">Jo\'natish</button>';
    if (!btn.includes('<button>') || !btn.includes('type=')) throw new Error('Button tegi xato');
});

test('HTML: Input turlari', () => {
    const types = ['text', 'password', 'email', 'number', 'checkbox', 'radio'];
    types.forEach(type => {
        const input = `<input type="${type}">`;
        if (!input.includes(`type="${type}"`)) throw new Error(`${type} input topilmadi`);
    });
});

test('HTML: Div tegi', () => {
    const div = '<div class="container"></div>';
    if (!div.includes('<div>') || !div.includes('class=')) throw new Error('Div tegi xato');
});

test('HTML: Span tegi', () => {
    const span = '<span class="highlight">Matn</span>';
    if (!span.includes('<span>')) throw new Error('Span tegi topilmadi');
});

test('HTML: Meta teglar', () => {
    const meta = '<meta charset="UTF-8"><meta name="viewport" content="width=device-width">';
    if (!meta.includes('charset=') || !meta.includes('viewport')) throw new Error('Meta teglari xato');
});

test('HTML: Script tegi', () => {
    const script = '<script src="script.js"></script>';
    if (!script.includes('<script>') || !script.includes('src=')) throw new Error('Script tegi xato');
});

test('HTML: Style tegi', () => {
    const style = '<style>.class { color: red; }</style>';
    if (!style.includes('<style>')) throw new Error('Style tegi topilmadi');
});

test('HTML: Select tegi', () => {
    const select = '<select><option>Option 1</option></select>';
    if (!select.includes('<select>') || !select.includes('<option>')) throw new Error('Select tegi xato');
});

test('HTML: Textarea tegi', () => {
    const textarea = '<textarea rows="4"></textarea>';
    if (!textarea.includes('<textarea>')) throw new Error('Textarea tegi topilmadi');
});

test('HTML: BR tegi (self-closing)', () => {
    const br = '<br>';
    if (!br.includes('<br>')) throw new Error('BR tegi topilmadi');
});

test('HTML: Semantic teglar', () => {
    const tags = ['header', 'nav', 'main', 'article', 'section', 'footer'];
    tags.forEach(tag => {
        if (!`<${tag}></${tag}>`.includes(`<${tag}>`)) throw new Error(`${tag} tegi xato`);
    });
});

test('HTML: DOCTYPE', () => {
    const doctype = '<!DOCTYPE html>';
    if (!doctype.includes('DOCTYPE')) throw new Error('DOCTYPE xato');
});


// ============================================================================
// 2. CSS TESTLARI (21-35)
// ============================================================================

console.log('\n=== CSS TESTLARI ===');

test('CSS: Class selector', () => {
    const css = '.class { color: red; }';
    if (!css.includes('.class')) throw new Error('Class selector topilmadi');
});

test('CSS: ID selector', () => {
    const css = '#header { background: blue; }';
    if (!css.includes('#header')) throw new Error('ID selector topilmadi');
});

test('CSS: Element selector', () => {
    const css = 'p { margin: 10px; }';
    if (!css.includes('p {')) throw new Error('Element selector xato');
});

test('CSS: Box model', () => {
    const box = 'margin: 10px; padding: 15px; border: 1px solid black;';
    if (!box.includes('margin') || !box.includes('padding') || !box.includes('border')) {
        throw new Error('Box model xossalari topilmadi');
    }
});

test('CSS: Flexbox', () => {
    const flex = 'display: flex; justify-content: center; align-items: center;';
    if (!flex.includes('display: flex')) throw new Error('Flexbox topilmadi');
});

test('CSS: Grid', () => {
    const grid = 'display: grid; grid-template-columns: 1fr 1fr;';
    if (!grid.includes('display: grid')) throw new Error('Grid topilmadi');
});

test('CSS: Position xossalari', () => {
    const positions = ['position: static;', 'position: relative;', 'position: absolute;', 'position: fixed;'];
    positions.forEach(pos => {
        if (!pos.includes('position:')) throw new Error('Position xossasi topilmadi');
    });
});

test('CSS: Media query', () => {
    const media = '@media (max-width: 768px) { .class { display: none; } }';
    if (!media.includes('@media') || !media.includes('max-width')) throw new Error('Media query xato');
});

test('CSS: Pseudo-class', () => {
    const pseudo = ':hover, :focus, :active';
    if (!pseudo.includes(':hover')) throw new Error('Pseudo-class topilmadi');
});

test('CSS: Pseudo-element', () => {
    const pseudo = '::before, ::after, ::first-line';
    if (!pseudo.includes('::before')) throw new Error('Pseudo-element topilmadi');
});

test('CSS: !important', () => {
    const css = 'color: red !important;';
    if (!css.includes('!important')) throw new Error('!important topilmadi');
});

test('CSS: Color qiymatlari', () => {
    const colors = ['color: red;', 'background-color: #fff;', 'border-color: rgb(0,0,0);'];
    colors.forEach(c => {
        if (!c.includes('color')) throw new Error('Color xossasi topilmadi');
    });
});

test('CSS: Font xossalari', () => {
    const font = 'font-size: 16px; font-family: Arial; font-weight: bold;';
    if (!font.includes('font-size') || !font.includes('font-family')) throw new Error('Font xossalari xato');
});

test('CSS: Z-index', () => {
    const z = 'z-index: 100;';
    if (!z.includes('z-index')) throw new Error('Z-index topilmadi');
});

test('CSS: Border radius', () => {
    const border = 'border-radius: 10px;';
    if (!border.includes('border-radius')) throw new Error('Border-radius topilmadi');
});


// ============================================================================
// 3. JAVASCRIPT TESTLARI (36-50)
// ============================================================================

console.log('\n=== JAVASCRIPT TESTLARI ===');

test('JS: Ozgaruvchi e\'lon qilish', () => {
    let x = 5;
    const y = 10;
    var z = 15;
    if (typeof x !== 'number' || typeof y !== 'number' || typeof z !== 'number') {
        throw new Error('Ozgaruvchi xato e\'lon qilingan');
    }
});

test('JS: Funksiya', () => {
    function greet(name) {
        return `Salom, ${name}!`;
    }
    if (greet('Ali') !== 'Salom, Ali!') throw new Error('Funksiya xato ishlaydi');
});

test('JS: Arrow funksiya', () => {
    const add = (a, b) => a + b;
    if (add(2, 3) !== 5) throw new Error('Arrow funksiya xato');
});

test('JS: Array', () => {
    const arr = [1, 2, 3, 4, 5];
    if (!Array.isArray(arr) || arr.length !== 5) throw new Error('Array xato');
});

test('JS: Array map', () => {
    const arr = [1, 2, 3];
    const mapped = arr.map(x => x * 2);
    if (mapped[0] !== 2 || mapped[1] !== 4 || mapped[2] !== 6) {
        throw new Error('map() xato ishlaydi');
    }
});

test('JS: Array filter', () => {
    const arr = [1, 2, 3, 4, 5];
    const filtered = arr.filter(x => x > 3);
    if (filtered.length !== 2 || filtered[0] !== 4) throw new Error('filter() xato');
});

test('JS: Array reduce', () => {
    const arr = [1, 2, 3, 4];
    const sum = arr.reduce((a, b) => a + b, 0);
    if (sum !== 10) throw new Error('reduce() xato');
});

test('JS: Object', () => {
    const obj = { name: 'Ali', age: 25 };
    if (obj.name !== 'Ali' || obj.age !== 25) throw new Error('Object xato');
});

test('JS: Object methods', () => {
    const obj = { a: 1, b: 2 };
    const keys = Object.keys(obj);
    const values = Object.values(obj);
    if (keys[0] !== 'a' || values[0] !== 1) throw new Error('Object methods xato');
});

test('JS: String methods', () => {
    const s = '  Hello World  ';
    if (s.trim() !== 'Hello World' || s.toUpperCase().includes('HELLO') === false) {
        throw new Error('String methods xato');
    }
});

test('JS: Spread operator', () => {
    const arr1 = [1, 2, 3];
    const arr2 = [...arr1, 4, 5];
    if (arr2.length !== 5 || arr2[0] !== 1) throw new Error('Spread operator xato');
});

test('JS: Destructuring', () => {
    const [a, b] = [1, 2];
    if (a !== 1 || b !== 2) throw new Error('Destructuring xato');
});

test('JS: Template literal', () => {
    const name = 'Ali';
    const greeting = `Salom, ${name}!`;
    if (greeting !== 'Salom, Ali!') throw new Error('Template literal xato');
});

test('JS: Promise', () => {
    const promise = new Promise((resolve, reject) => {
        resolve('Success');
    });
    if (!(promise instanceof Promise)) throw new Error('Promise xato');
});

test('JS: Set', () => {
    const set = new Set([1, 2, 3, 2, 1]);
    if (set.size !== 3) throw new Error('Set xato');
});


// ============================================================================
// NATICHA
// ============================================================================

console.log('\n=== TEST NATIJALARI ===');
console.log(`Umumiy testlar: ${testResults.passed + testResults.failed}`);
console.log(`Utgan testlar: ${testResults.passed}`);
console.log(`Xatoliklar: ${testResults.failed}`);

// Brauzerda natijalarni chiqarish
if (typeof document !== 'undefined') {
    const resultsDiv = document.getElementById('test-results');
    if (resultsDiv) {
        resultsDiv.innerHTML = `
            <h2>Test Natijalari</h2>
            <p>Umumiy: ${testResults.passed + testResults.failed}</p>
            <p class="passed">Utgan: ${testResults.passed}</p>
            <p class="failed">Xatolik: ${testResults.failed}</p>
            <ul>
                ${testResults.tests.map(t => 
                    `<li class="${t.status.toLowerCase()}">${t.name} - ${t.status}</li>`
                ).join('')}
            </ul>
        `;
    }
}

module.exports = testResults;
