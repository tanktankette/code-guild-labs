import string
import re


def scrub_numbers(input: str) -> str:
    return re.sub(r"\d", "", input)

def gentle_clean(input: str) -> str:
    input = re.sub(r"[-_]", " ", input)
    return input.replace("  ", " ")

def clean_data(input: str) -> str:
    return gentle_clean(scrub_numbers(input)).strip()

def some_scrubber(input: str) -> str:
    return re.sub(r"(?<=[\w\.]) ", "", input).replace("  ", " ")

def mr_clean(input: str) -> str:
    i = 0
    input = list(input)
    while i < len(input):
        input.insert(i, " ")
        i += 2
    return "".join(input)

def ms_clean(input: str) -> str:
    input = input.split(" ")
    out = []
    for s in input:
        out.append(f"{s[0]}{len(s) - 2}{s[len(s) - 1]}")
    return " ".join(out)

def strong_cleaner(input: str) -> str:
    c = input[0]
    return c + re.sub(r"[!@#$%^&*()\dA-Z]", "", input)

def extracto(input):
    total = 0
    for n in string.digits:
        total += int(n) * input.count(n)
    return total

print(scrub_numbers('Be9autiful9 i4s be2tter th4an ug42ly'))

print(gentle_clean('Explicit_is-better_than -implicit'))

print(clean_data('  42Simple-is_better_than-compl9ex   '))
print(some_scrubber('F l a t   i s   b e t t e r   t h a n   n e s t e d . '))
print(mr_clean('Sparse is better than dense'))
print(ms_clean('Readability counts'))
print(strong_cleaner('Err@#%$ors sho@#$@#$uld nev1!$#@er pass sile&I&&*(ntly'))
print(extracto('1S2pe3cia4l ca5ses ar6en\'t sp7ecial en8ough to b9reak the r0ules.'))
print(extracto('2S4pe6cia8l ca0ses ar2en\'t sp4ecial en6ough to b8reak the r0ules.'))
print(extracto('3S6pe9cia2l ca5ses ar8en\'t sp1ecial en4ough to b7reak the r0ules.'))
