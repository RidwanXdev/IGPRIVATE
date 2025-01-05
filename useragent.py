import random

class Useragent:
    def generate_useragent(self):
        # Daftar komponen yang bisa diacak
        app_versions = [
            "273.1.0.16.72", "272.0.0.16.70", "271.1.0.15.69",
            "270.0.0.15.65", "269.0.0.23.64", "268.1.0.18.61",
            "274.0.0.20.75", "275.1.0.18.77", "276.1.0.22.80"
        ]
        android_versions = [
            "29/10", "30/11", "28/9", "31/12", "32/13", "27/8",
            "33/14", "34/15", "35/16", "36/17"
        ]
        ios_versions = [
            "iOS 15.1", "iOS 16.0", "iOS 14.4", "iPadOS 16.2", "iOS 17.1",
            "iOS 16.5", "iOS 17.2", "iOS 18.0"
        ]
        windows_versions = [
            "Windows 10", "Windows 11", "Windows 8.1", "Windows 7", "Windows 8",
            "Windows 12", "Windows 10 Pro"
        ]
        dpis = [
            "320dpi", "480dpi", "640dpi", "213dpi", "240dpi", "160dpi",
            "420dpi", "560dpi", "800dpi"
        ]
        resolutions = [
            "1080x2400", "720x1600", "1080x2340", "1440x3200",
            "1080x2280", "1080x1920", "720x1280", "1920x1080",
            "1440x2560", "1440x2960", "2560x1440"
        ]
        languages = [
            "en_US", "id_ID", "zh_CN", "hi_IN", "ar_SA", "es_ES",
            "ru_RU", "pt_BR", "fr_FR", "ja_JP", "de_DE", "it_IT", "ko_KR"
        ]

        models = {
            "vivo": [
                "vivo Y20", "vivo X70 Pro", "vivo V21", "vivo Y33s", "vivo V25e", "vivo Y91C", "vivo X60 Pro",
                "vivo X80 Pro", "vivo V23 5G", "vivo Y73", "vivo Y12s", "vivo X50 Pro", "vivo V15 Pro", "vivo V19",
                "vivo Y19"
            ],
            "samsung": [
                "Galaxy S21", "Galaxy A12", "Galaxy Z Flip", "Galaxy Note 20", "Galaxy A72", "Galaxy M32", "Galaxy Z Fold 3",
                "Galaxy S22", "Galaxy Z Fold 4", "Galaxy A53", "Galaxy S20 FE", "Galaxy A32", "Galaxy M12", "Galaxy A51",
                "Galaxy S10e"
            ],
            "meizu": [
                "Meizu 16th", "Meizu M5 Note", "Meizu 18 Pro", "Meizu C9", "Meizu X8", "Meizu 17", "Meizu 16X",
                "Meizu 19 Pro", "Meizu 18s", "Meizu M6", "Meizu M3 Note", "Meizu 16s Pro", "Meizu X9", "Meizu 15 Plus",
                "Meizu M2"
            ],
            "oppo": [
                "OPPO Reno6", "OPPO A54", "OPPO Find X3 Pro", "OPPO F11", "OPPO A15", "OPPO A92", "OPPO Reno5",
                "OPPO Reno7", "OPPO Find X5 Pro", "OPPO A73", "OPPO A53", "OPPO F19 Pro", "OPPO A74", "OPPO F19",
                "OPPO A16"
            ],
            "xiaomi": [
                "Redmi Note 11", "Xiaomi 12", "Redmi Note 10 Pro", "Redmi Note 9 Pro", "Xiaomi Mi 11 Lite", "Xiaomi Mi 10", "Xiaomi 11T Pro",
                "Xiaomi 13 Pro", "Xiaomi 12T", "Redmi Note 8 Pro", "Xiaomi Mi 9", "Redmi K40", "Xiaomi Mi 11 Ultra", "Redmi 10",
                "Xiaomi 11X"
            ],
            "realme": [
                "Realme C21", "Realme GT Neo 2", "Realme 9 Pro+", "Realme X3", "Realme 8 Pro", "Realme X50", "Realme 7i",
                "Realme 10 Pro", "Realme GT 2 Pro", "Realme Narzo 30", "Realme C25s", "Realme 6 Pro", "Realme 9i", "Realme C35",
                "Realme X7 Max"
            ],
            "infinix": [
                "Infinix Zero X", "Infinix Note 11", "Infinix Smart 5", "Infinix Zero Ultra", "Infinix Note 12", "Infinix Zero 8",
                "Infinix Zero 30", "Infinix Hot 12 Pro", "Infinix Note 10", "Infinix S5 Pro", "Infinix Hot 9", "Infinix Note 7",
                "Infinix Zero 6", "Infinix Smart 4", "Infinix Note 8"
            ],
            "huawei": [
                "Huawei P40", "Huawei Mate 40 Pro", "Huawei Nova 9", "Huawei P30 Pro", "Huawei Y9a", "Huawei P20", "Huawei Mate 30 Pro",
                "Huawei P50 Pro", "Huawei Mate 50", "Huawei Nova 7i", "Huawei P40 Lite", "Huawei Y7a", "Huawei Mate Xs", "Huawei P20 Pro",
                "Huawei Y9s"
            ],
            "andromax": [
                "Andromax A", "Andromax R2", "Andromax E2", "Andromax L", "Andromax Q", "Andromax ES", "Andromax M2", "Andromax B", 
                "Andromax C", "Andromax F", "Andromax G", "Andromax S", "Andromax V", "Andromax Z", "Andromax J"
            ],
            "poco": [
                "Poco X3 NFC", "Poco M3", "Poco X4 Pro", "Poco F3", "Poco F2 Pro", "Poco M2 Pro", "Poco C3",
                "Poco X5 Pro", "Poco M4 Pro", "Poco F4", "Poco X3 Pro", "Poco M2", "Poco X3 GT", "Poco M5", "Poco X4"
            ],
            "iphone": [
                "iPhone 12 Pro", "iPhone 13", "iPhone 14 Pro", "iPhone XR", "iPhone 11", "iPhone SE 2020",
                "iPhone 15", "iPhone 14 Pro Max", "iPhone 13 Pro Max", "iPhone 12 Mini", "iPhone 14", "iPhone 13 Mini",
                "iPhone 12", "iPhone 15 Pro", "iPhone 15 Plus"
            ],
            "ipad": [
                "iPad Pro 12.9", "iPad Air 4", "iPad Mini 6", "iPad Pro 11", "iPad 9th Gen", "iPad Air 5",
                "iPad Pro 11 (2022)", "iPad Air (2023)", "iPad Pro 10.5", "iPad 8th Gen", "iPad Mini 5", "iPad 7th Gen",
                "iPad Pro 12.9 (2021)", "iPad Mini 7", "iPad 10th Gen"
            ],
            "windows": [
                "Surface Pro 7", "Dell XPS 13", "HP Spectre x360", "Lenovo ThinkPad", "Acer Aspire 5", "Microsoft Surface Laptop",
                "Microsoft Surface Laptop 4", "Lenovo Legion 5", "HP Envy 13", "Asus ZenBook 14", "Surface Laptop Go", "Acer Swift 3",
                "Microsoft Surface Pro 8", "Lenovo Yoga Slim 7", "HP Pavilion 14"
            ],
            "nokia": [
                "Nokia 5.3", "Nokia 8.1", "Nokia X20", "Nokia G10", "Nokia 6.2", "Nokia 7.2", "Nokia 2.4",
                "Nokia 8.3", "Nokia G50", "Nokia 7.1", "Nokia 6.1", "Nokia 5.1", "Nokia 3.4", "Nokia X10", "Nokia 9 PureView"
            ]
        }

        processors = {
            "vivo": ["sdm710", "mt6765", "dimensity800", "dimensity1200", "helioP35"],
            "samsung": ["exynos2100", "snapdragon888", "exynos9611"],
            "meizu": ["snapdragon845", "dimensity1200", "exynos9810"],
            "oppo": ["dimensity1200", "snapdragon888", "helioP95"],
            "xiaomi": ["snapdragon870", "snapdragon720G", "dimensity1200"],
            "realme": ["snapdragon855", "dimensity1000", "dimensity800U"],
            "infinix": ["helioG90T", "snapdragon730G", "dimensity700"],
            "huawei": ["kirin9000", "kirin810", "kirin710F"],
            "andromax": ["snapdragon425", "snapdragon430", "snapdragon636"],
            "poco": ["snapdragon870", "snapdragon860", "snapdragon720G"],
            "iphone": ["A15 Bionic", "A14 Bionic", "A13 Bionic"],
            "ipad": ["A14 Bionic", "A12 Bionic", "A13 Bionic"],
            "windows": ["intelI7", "intelI5", "amdRyzen5"],
            "nokia": ["snapdragon630", "snapdragon660", "snapdragon710"]
        }

        # Pilih secara acak komponen-komponen
        app_version = random.choice(app_versions)
        dpi = random.choice(dpis)
        resolution = random.choice(resolutions)
        language = random.choice(languages)

        # Pilih brand secara acak
        brand = random.choice(list(models.keys()))
        model = random.choice(models[brand])
        processor = random.choice(processors[brand])

        # Generate random ID untuk ditambahkan di akhir
        random_id = random.randint(100000000, 999999999)

        if brand in ["iphone", "ipad"]:
            ios_version = random.choice(ios_versions)
            v1 = f"Instagram {app_version} {ios_version} ({resolution}; {dpi}; {model}; {processor}; {language}; {random_id})"
            v2 = f"Instagram {app_version} {ios_version} ({resolution}; {dpi}; {model}; {processor}; {language})"
            ua_random = random.choice([v1, v2])
            return ua_random
        elif brand == "windows":
            windows_version = random.choice(windows_versions)
            v1 = f"Instagram {app_version} {windows_version} ({resolution}; {dpi}; {model}; {processor}; {language}; {random_id})"
            v2 = f"Instagram {app_version} {windows_version} ({resolution}; {dpi}; {model}; {processor}; {language})"
            ua_random = random.choice([v1, v2])
            return ua_random
        else:
            android_version = random.choice(android_versions)
            v1 = f"Instagram {app_version} Android ({android_version}; {dpi}; {resolution}; {brand}; {model}; {processor}; {language}; {random_id})"
            v2 = f"Instagram {app_version} Android ({android_version}; {dpi}; {resolution}; {brand}; {model}; {processor}; {language})"
            ua_random = random.choice([v2, v1])
            return ua_random

    def useragent_api(self):
        return self.generate_useragent()
    
    def replace_instagram_with_barcelona(self, text):
        return text.replace("Instagram", "Barcelona")
    
    def useragent_threads(self):
        new = random.choice(["Threads/289.0.0.77.109 CFNetwork/1390 Darwin/22.0.0 (Barcelona; Android 10; Scale/3.00)","Threads/289.0.0.77.109 CFNetwork/1390 Darwin/22.0.0 (Barcelona; iPhone; iOS 15.4; Scale/3.00)","Threads/289.0.0.77.109 CFNetwork/1390 Darwin/22.0.0 (Barcelona; iPhone 13 Pro; iOS 16.0; Scale/3.00)","Threads/289.0.0.77.109 CFNetwork/1390 Darwin/22.0.0 (Barcelona; iPhone 12; iOS 14.5; Scale/2.00)","Threads/289.0.0.77.109 CFNetwork/1390 Darwin/22.0.0 (Barcelona; Android 11; Pixel 4; Scale/3.00)","Threads/289.0.0.77.109 CFNetwork/1390 Darwin/22.0.0 (Barcelona; Samsung Galaxy S20; Android 10; Scale/3.00)","Threads/289.0.0.77.109 CFNetwork/1390 Darwin/22.0.0 (Barcelona; Xiaomi Mi 9; Android 9; Scale/3.00)"])
        input_text = self.generate_useragent()
        output_text = self.replace_instagram_with_barcelona(input_text)
        crot = random.choice([new, output_text])
        return output_text
        