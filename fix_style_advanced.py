import os
import subprocess
import textwrap

MAX_LINE_LENGTH = 120

def fix_file(path):
    with open(path, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    # حذف خط خالی انتهای فایل (W391)
    while lines and lines[-1].strip() == '':
        lines.pop()

    # اضافه کردن newline در انتهای فایل (W292)
    if lines and not lines[-1].endswith('\n'):
        lines[-1] += '\n'

    # اصلاح فاصله قبل از تعریف تابع یا کلاس (E302)
    fixed_lines = []
    for i, line in enumerate(lines):
        if line.strip().startswith(('def ', 'class ')):
            if i >= 1 and lines[i-1].strip() != '':
                fixed_lines.append('\n')
        fixed_lines.append(line)

    # شکستن خطوط طولانی (E501)
    final_lines = []
    for line in fixed_lines:
        if len(line) > MAX_LINE_LENGTH and ('=' in line or ',' in line):
            wrapped = textwrap.wrap(line, width=MAX_LINE_LENGTH)
            final_lines.extend([w + '\n' for w in wrapped])
        else:
            final_lines.append(line)

    with open(path, 'w', encoding='utf-8') as f:
        f.writelines(final_lines)

def walk_and_fix(root):
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            if filename.endswith('.py'):
                full_path = os.path.join(dirpath, filename)
                fix_file(full_path)
                print(f'✅ Fixed: {full_path}')

def run_formatter(tool):
    try:
        subprocess.run([tool, '.'], check=True)
        print(f'✨ Formatter applied: {tool}')
    except FileNotFoundError:
        print(f'⚠️ Formatter not found: {tool} (skipped)')

if __name__ == '__main__':
    walk_and_fix('.')
    run_formatter('black')      # اگر نصب باشه، اجرا می‌شه
    run_formatter('autopep8')   # اگر نصب باشه، اجرا می‌شه
