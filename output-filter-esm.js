// output-filter-esm.js

export class OutputFilter {
    constructor(options = {}) {
        this.verbose = options.verbose ?? false;
        this.maxLines = options.maxLines ?? 50;
        this.maxChars = options.maxChars ?? 5000;
    }

    filter(output = '', commandType = 'generic') {
        const lines = output.split('\n');
        const originalLines = lines.length;
        const originalSize = output.length;

        let result = output;
        let truncated = false;
        let truncatedAt = null;

        if (!this.verbose) {
            if (originalLines > this.maxLines) {
                result = lines.slice(0, this.maxLines).join('\n') + `\n...\n[Truncated to ${this.maxLines} lines]`;
                truncated = true;
                truncatedAt = 'lines';
            } else if (originalSize > this.maxChars) {
                result = output.substring(0, this.maxChars) + `\n...\n[Truncated to ${this.maxChars} chars]`;
                truncated = true;
                truncatedAt = 'chars';
            }
        }

        return {
            result,
            metadata: {
                filtered: truncated,
                truncated,
                truncatedAt,
                originalLines,
                originalSize,
                displayedLines: this.maxLines,
                displayedChars: this.maxChars,
                commandType
            }
        };
    }
}

export function detectCommandType(code = '') {
    if (code.includes('git')) return 'git';
    if (code.includes('ls') || code.includes('cd')) return 'filesystem';
    if (code.includes('curl') || code.includes('http')) return 'network';
    if (code.includes('import ') || code.includes('def ')) return 'python';
    return 'generic';
}
