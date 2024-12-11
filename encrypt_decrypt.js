const fs = require('fs');

const ENCRYPTION_KEY = "QWERTY";
const match_brackets = /([^\[]*)]/;
const match_inner_quote = /"(.*)"/;

function encryption(input_text, encrypt) {
    let output = [];
    const KEY_MAX_INDEX = ENCRYPTION_KEY.length;

    for (const [index, c] of Array.from(input_text).entries()) {
        const CodePointInput = c.charCodeAt(0);
        const codePointKey = ENCRYPTION_KEY[index % KEY_MAX_INDEX].codePointAt(0);

        let output_char = '';
        if (encrypt) {
            output_char = String.fromCodePoint(CodePointInput + codePointKey);
        } else {
            output_char = String.fromCodePoint(CodePointInput - codePointKey);
        }
        output.push(output_char);
    }

    return output.join('');
}

function readSave(input_path, output_path, encrypt) {
    const fileContent = fs.readFileSync(input_path, 'utf-8');
    const lines = fileContent.split(/\r?\n/);
    const output = lines.map(line => {
        if (line[0] === '\0' || line[0] === ' ') return null;

        let match;
        if ((match = match_brackets.exec(line)) !== null) {
            const changed_text = encryption(match[1], encrypt);
            return `[${changed_text}]\n`;
        } else {
            const [key, value] = line.split("=");
            const changed_key = encryption(key, encrypt);
            if (!changed_key) return null;

            let changed_val;
            if ((match = match_inner_quote.exec(value)) !== null) {
                changed_val = encryption(match[1], encrypt);
            } else {
                changed_val = "";
            }

            return `${changed_key}="${changed_val}"\n`;
        }
    }).filter(line => line !== null);

    fs.writeFileSync(output_path, output.join(''));
}

const inputPath = process.argv[2];
const outputPath = process.argv[3];
const mode = process.argv[4] === "encrypt";

readSave(inputPath, outputPath, mode);
