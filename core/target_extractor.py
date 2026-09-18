# اضافه کردن نام برنامه ها
# Adding application names
class TargetExtractor:


    def __init__(self):

        self.targets = {

            "chrome": [
                "chrome",
                "کروم",
                "مرورگر"
            ],

            "notepad": [
                "notepad",
                "نوت پد",
                "دفترچه"
            ],

            "calculator": [
                "calculator",
                "ماشین حساب"
            ],

            "vscode": [
                "vscode",
                "visual studio code",
                "وی اس کد"
            ]

        }



    def extract(self, command):

        command = command.lower().strip()


        for target, keywords in self.targets.items():

            for keyword in keywords:

                if keyword in command:

                    return target


        return None