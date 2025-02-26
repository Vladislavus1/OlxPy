# [OlxPy](https://pypi.org/project/OlxPy)

This package simplifies the extraction of data from OLX websites ([olx.ua](https://www.olx.ua), [olx.pl](https://www.olx.pl), [olx.kz](https://www.olx.kz)). It allows users to programmatically retrieve listings, such as real estate, vehicles, or job offers, directly from OLX.

## How to use it?

First you need to download this package to your computer system by doing this command:

    git clone https://github.com/Vladislavus1/OlxPy.git

Now it's ready to work. In your python file, you'll need to import this package:

    from OlxPy import OlxParser

You've just imported an ```OlxParser``` class. Then you need to create a class object:

    var_name = OlxParser()

```OlxParser``` has one available argument ```-logging=True/False(True by default)```. Logging is responsible for printing detailed information about parsing process.
To start parsing products from OLX, you'll need to use ```OlxParser``` method called ```get_products(url, amount)``` (where ```amount``` is not necessary argument):

    url_example = "https://www.olx.ua/uk/elektronika/"
    parser = OlxParser()
    parser.get_products(url_example)

After you run a code you should see this messages:

    Parsing https://www.olx.ua/uk/elektronika/?page=1 (response code: 200) (done)
    Parsing https://www.olx.ua/uk/elektronika/?page=2 (response code: 200) (done)
    Parsing https://www.olx.ua/uk/elektronika/?page=3 (response code: 200) (done)
    ...
    
These messages are saying that parsing ad's urls on each page is done successfully.
After that you'll start to see this messages about "Getting information":

    Getting information:
      • https://www.olx.ua/d/uk/obyavlenie/libertys-f12-m-b-2l-nova-kavomashina-prodazh-IDWkYXf.html (response code: 200) (done)
      • https://www.olx.ua/d/uk/obyavlenie/telefon-huawei-mate-30-pro-8-256gb-dual-IDWDPJw.html (response code: 200) (done)
      • https://www.olx.ua/d/uk/obyavlenie/novinka-bezdrotov-navushniki-arpods-3-groskop-chp-huilian-a10-IDUyrz1.html (response code: 200) (done)
      • https://www.olx.ua/d/uk/obyavlenie/prodam-aparat-uf-vipromnyuvannya-novator-IDTzLdy.html (response code: 200) (done)
      • https://www.olx.ua/d/uk/obyavlenie/blok-zhivlennya-12v-dlya-led-jinbo-jlv-12400kb-IDPSL4Y.html (response code: 200) (done)
      • https://www.olx.ua/d/uk/obyavlenie/detskiy-ingalyator-kompressornyy-microlife-neb-400-IDWeuv6 (response code: 200) (done)
      ...

Now your program is on a phase where main information is picking.
After all that ```get_products``` method will just return a list full of ```OlxAd``` class objects. ```OlxAd``` class objects contains: ```ad_title```, ```ad_price```, ```ad_url```, ```ad_images(list full of ad's images urls)```.
Here's example:

    from OlxPy import OlxParser
    
    url_example = "https://www.olx.ua/uk/elektronika/"
    parser = OlxParser()
    ads = parser.get_products(url_example)
    print(ads[0].ad_title, ads[0].ad_price, ads[0].ad_url, ads[0].ad_images)

Output:

    Преміум Якість! BatteryPack MagSafe 5000 mAh/ PowerBank/ Apple 699 грн. https://www.olx.ua/d/uk/obyavlenie/premum-yakst-batterypack-magsafe-5000-mah-powerbank-apple-IDWtbYN.html ['https://ireland.apollo.olxcdn.com:443/v1/files/yx7cd
    0u2t2c-UA/image;s=750x1000', 'https://ireland.apollo.olxcdn.com:443/v1/files/grzza7hf5ycj1-UA/image;s=750x1000', 'https://ireland.apollo.olxcdn.com:443/v1/files/oohfrff0t99c1-UA/image;s=750x1000']

As you see everything is working just fine!

## Error logs

In rare cases you can face some errors. Some of them will give you ```error_logs.txt```, **what you need to do with them?**
First, try to fix url or restart the code, if it's not working, please provide ```error_logs.txt``` to me, and I will try to fix it as soon as possible.

## Disclaimer

This project is still in a phase of developing, so the risk of facing errors is really high. Anyway if you face some of them please provide it to [GitHub Issues](https://github.com/Vladislavus1/OlxPyApi/issues), I will be really grateful.

#

Thanks for attention!
