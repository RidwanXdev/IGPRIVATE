import random

class Useragent:
    def generate_useragent(self):
        # Daftar komponen yang diperbarui
        app_versions = [
            "302.0.0.18.113", "301.1.0.16.112", "300.0.0.15.110",
            "299.0.0.15.108", "298.1.0.12.106", "297.0.0.11.104",
            "303.1.0.20.115", "304.0.0.22.117", "305.1.0.25.120",
            "306.0.0.30.125", "307.0.0.33.130", "308.0.0.36.135",
            "309.0.0.40.140", "310.0.0.45.150", "311.0.0.50.160",
            "312.0.0.55.170", "313.0.0.60.180", "314.0.0.65.190"
        ]
        android_versions = [
            "33/14", "34/15", "32/13", "31/12", "30/11", "29/10",
            "28/9", "27/8", "35/16", "36/17"
        ]
        ios_versions = [
            "iOS 16.4", "iOS 17.0", "iOS 15.5", "iPadOS 16.6", "iOS 18.0",
            "iOS 17.1", "iOS 14.8", "iOS 15.2", "iOS 17.5", "iOS 16.3"
        ]
        dpis = [
            "320dpi", "480dpi", "640dpi", "213dpi", "240dpi", "160dpi",
            "420dpi", "560dpi", "800dpi", "300dpi"
        ]
        resolutions = [
            "1080x2400", "720x1600", "1440x3200", "1080x2340", "1920x1080",
            "1440x2560", "2560x1440", "1280x720", "1440x2960", "3840x2160"
        ]
        languages = [
            "en_US", "id_ID", "zh_CN", "hi_IN", "ar_SA", "es_ES",
            "ru_RU", "pt_BR", "fr_FR", "ja_JP", "de_DE", "it_IT", "ko_KR", "vi_VN"
        ]

        models = {
            "sony": ["Xperia 1 IV", "Xperia 5 III", "Xperia 10 IV", "Xperia XZ2", "Xperia Z5"],
            "lg": ["LG Velvet", "LG Wing", "LG G8 ThinQ", "LG V60 ThinQ", "LG Q60"],
            "oneplus": ["OnePlus 11", "OnePlus 10 Pro", "OnePlus Nord 2", "OnePlus 8T", "OnePlus 7 Pro"],
            "google": ["Pixel 6", "Pixel 7 Pro", "Pixel 5", "Pixel 4a", "Pixel 3 XL"],
            "xiaomi": ["Redmi Note 12", "Mi 11 Ultra", "Xiaomi 13 Pro", "Xiaomi 12T", "Xiaomi Mi 10"],
            "oppo": ["Find X6 Pro", "Reno 8", "OPPO A77", "OPPO F21 Pro", "OPPO K10"],
            "samsung": ["Galaxy S23 Ultra", "Galaxy Z Fold 5", "Galaxy A54", "Galaxy Note 20", "Galaxy M14"],
            "apple": ["iPhone 14 Pro", "iPad Pro 12.9", "iPhone 13 Mini", "iPhone SE 2020", "iPhone 15"]
        }

        processors = {
            "sony": ["Snapdragon 8 Gen 2", "Snapdragon 888", "Snapdragon 695", "Exynos 2100", "Dimensity 900"],
            "lg": ["Snapdragon 765G", "Snapdragon 845", "Dimensity 900", "Snapdragon 820", "Helio G95"],
            "oneplus": ["Snapdragon 8 Gen 2", "Dimensity 1200", "Snapdragon 778G", "Snapdragon 870", "Dimensity 810"],
            "google": ["Tensor G2", "Tensor", "Snapdragon 765G", "Snapdragon 730G", "Exynos 850"],
            "xiaomi": ["Snapdragon 870", "Dimensity 920", "Snapdragon 778G", "Snapdragon 855", "Dimensity 8100"],
            "oppo": ["Dimensity 9000", "Snapdragon 888", "Helio G96", "Snapdragon 720G", "Dimensity 1200"],
            "samsung": ["Exynos 2200", "Snapdragon 8 Gen 2", "Exynos 1280", "Snapdragon 855", "Dimensity 1080"],
            "apple": ["A16 Bionic", "M1 Pro", "A14 Bionic", "A15 Bionic", "M2"]
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

        if brand in ["apple"]:
            ios_version = random.choice(ios_versions)
            useragent = f"Instagram {app_version} {ios_version} ({resolution}; {dpi}; {model}; {processor}; {language}; {random_id})"
        else:
            android_version = random.choice(android_versions)
            useragent = f"Instagram {app_version} Android ({android_version}; {dpi}; {resolution}; {brand}; {model}; {processor}; {language}; {random_id})"

        return useragent

    def useragent_api(self):
        return self.generate_useragent()
    
    def replace_instagram_with_barcelona(self, text):
        return text.replace("Instagram", "Barcelona")
    
    def useragent_threads(self):
        new = random.choice(["Threads/289.0.0.77.109 CFNetwork/1390 Darwin/22.0.0 (Barcelona; Android 10; Scale/3.00)","Threads/289.0.0.77.109 CFNetwork/1390 Darwin/22.0.0 (Barcelona; iPhone; iOS 15.4; Scale/3.00)","Threads/289.0.0.77.109 CFNetwork/1390 Darwin/22.0.0 (Barcelona; iPhone 13 Pro; iOS 16.0; Scale/3.00)","Threads/289.0.0.77.109 CFNetwork/1390 Darwin/22.0.0 (Barcelona; iPhone 12; iOS 14.5; Scale/2.00)","Threads/289.0.0.77.109 CFNetwork/1390 Darwin/22.0.0 (Barcelona; Android 11; Pixel 4; Scale/3.00)","Threads/289.0.0.77.109 CFNetwork/1390 Darwin/22.0.0 (Barcelona; Samsung Galaxy S20; Android 10; Scale/3.00)","Threads/289.0.0.77.109 CFNetwork/1390 Darwin/22.0.0 (Barcelona; Xiaomi Mi 9; Android 9; Scale/3.00)"])
        input_text = self.generate_useragent()
        output_text = self.replace_instagram_with_barcelona(input_text)
        crot = random.choice([new, output_text])
        return output_text(Useragent().useragent_threads())       
