from core.target_extractor import TargetExtractor


extractor = TargetExtractor()


commands = [
    "کروم رو باز کن",
    "مرورگر رو اجرا کن",
    "نوت پد رو باز کن",
    "وی اس کد رو اجرا کن"
]


for command in commands:

    result = extractor.extract(command)

    print(command)
    print("Target:", result)
    print("----------------")