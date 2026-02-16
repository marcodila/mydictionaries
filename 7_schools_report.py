"""
Process the JSON file named school_data.json. Display only those schools 
that are part of the ACC, Big 12, Big Ten and SEC divisons.

Copy that info here:

"NCAA/NAIA conference number football (IC2020)","372","American Athletic Conference"
"NCAA/NAIA conference number football (IC2020)","108","Big Twelve Conference"
"NCAA/NAIA conference number football (IC2020)","107","Big Ten Conference"
"NCAA/NAIA conference number football (IC2020)","130","Southeastern Conference"


Display report for all universities that have a graduation rate for Women over 75%
Display report for all universities that have a total price for in-state students living off campus over $60,000



"""

import json

schools = json.load(open("school_data.json", "r"))

print(f"Records Loaded: {len(schools)}")
print()

school_codes = {372, 108, 107, 130}

# Filter Power Conference Schools
school_conf = [
    school for school in schools
    if school.get("NCAA", {}).get("NAIA conference number football (IC2020)", 0) in school_codes
]

print(f"Total Power Schools Found: {len(school_conf)}")
print()


# Graduation Report

count = 0

for school in school_conf:
    women_grad_rate = school.get("Graduation rate  women (DRVGR2020)")

    if women_grad_rate is not None and women_grad_rate > 75:
        count += 1
        print(f"University: {school['instnm']}")
        print(f"Graduation Rate for Women: {women_grad_rate}%")
        print()

print(f"Total Schools Shown: {count}")
print()


# Price Report

count = 0

for school in school_conf:
    price_off_instate = school.get(
        "Total price for in-state students living off campus (not with family)  2020-21 (DRVIC2020)"
    )

    if price_off_instate is not None and price_off_instate > 60000:
        count += 1
        print(f"University: {school['instnm']}")
        print(f"Total price for in-state students living off campus: ${price_off_instate:,.2f}")
        print()

print(f"Total Schools Shown: {count}")
print()






