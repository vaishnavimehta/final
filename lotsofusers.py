from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from flask import Flask, url_for

from database_setup import Base,Product,Event,Bestseller,Ware,Catalog

engine = create_engine('sqlite:///restaurantmenuwithusers.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

event1 = Event(name="AAKAR Delhi", location="Delhi", month="August", year="2017-18", image="aakardelhi.png" )
session.add(event1)
session.commit()

event2 = Event(name="AAKAR Ahemdabad", location="Ahemdabad", month="September", year="2017-18", image="aakarahm.png" )
session.add(event2)
session.commit()

event3 = Event(name="AAKAR Kolkata", location="Kolkata", month="December", year="2017-18", image="upcoming.jpg" )
session.add(event3)
session.commit()

event4 = Event(name="AAHAR Delhi", location="Delhi", month="March", year="2018-19", image="upcoming.jpg" )
session.add(event4)
session.commit()

event5 = Event(name="AAKAR Delhi", location="Delhi", month="August", year="2018-19", image="upcoming.jpg" )
session.add(event5)
session.commit()

product1 = Product(name="Magic Rectangualar Chaffing Dish", catagory="CD", id="CD-601", size="18, 20 lt", price=500, polish="Glossy", image="2.1.jpg" )
session.add(product1)
session.commit()

product2 = Product(name="Magic Rose gold Rectangular Chaffing Dish", catagory="CD", id="CD-602", size="18, 20 lt", price=500, polish="Glossy", image="2.2.jpg" )
session.add(product2)
session.commit()

product3 = Product(name="Magic coloured Rectangular Chaffing Dish", catagory="CD", id="CD-603", size="18, 20 lt", price=500, polish="Glossy", image="2.3.jpg" )
session.add(product3)
session.commit()

product4 = Product(name="Pipe jug", catagory="TW", id="TW-701", size="standard", price=500, polish="Glossy", image="7.1.jpg" )
session.add(product4)
session.commit()

product5 = Product(name="Pipe jug 2", catagory="TW", id="TW-702", size="standard", price=500, polish="Mat", image="7.2.jpg" )
session.add(product5)
session.commit()

product6 = Product(name="Balti", catagory="HW", id="HW-801", size="12, 13, 14, 15, 16", price=500, polish="Glossy", image="9.1.jpg" )
session.add(product6)
session.commit()

product7 = Product(name="Praat", catagory="HW", id="HW-802", size="14-22 inch", price=500, polish="Glossy", image="9.2.jpg" )
session.add(product7)
session.commit()

product8 = Product(name="Bar Trolley", catagory="TB", id="TB-501", size="standard", price=500, polish="Glossy", image="10.1.jpg" )
session.add(product8)
session.commit()

product9 = Product(name="Barbecue Table", catagory="TB", id="TB-502", size="standard", price=500, polish="Glossy", image="10.1.jpg" )
session.add(product9)
session.commit()

product10 = Product(name="Tikki Counter", catagory="CN", id="CN-901", size="standard", price=500, polish="Mat and Glossy", image="14.1.jpg" )
session.add(product10)
session.commit()

product11 = Product(name="Dosa Counter", catagory="CN", id="CN-902", size="standard", price=500, polish="Mat and Glossy", image="14.2.jpg" )
session.add(product11)
session.commit()

product12 = Product(name="Magic Gold Rectangular Chaffing Dish", catagory="CD", id="CD-604", size="18, 20 lt", price=500, polish="Glossy", image="2.4.jpg" )
session.add(product12)
session.commit()

product13 = Product(name="Magic 3 leg Rectangular Chaffing Dish", catagory="CD", id="CD-605", size="18, 20 lt", price=500, polish="Glossy", image="2.5.jpg" )
session.add(product13)
session.commit()

product14 = Product(name="Square Chaffing Dish", catagory="CD", id="CD-606", size="12 X 13", price=500, polish="Glossy", image="2.6.jpg" )
session.add(product14)
session.commit()

product15 = Product(name="Rectangular Tent and Hotelware Chaffing Dish", catagory="CD", id="CD-607", size="13, 15, 18, 20 lt", price=500, polish="Glossy", image="2.7.jpg" )
session.add(product15)
session.commit()

product16 = Product(name="Sqaure Double Patti Hydraulic Chaffing Dish", catagory="CD", id="CD-608", size="12 X 13", price=500, polish="Glossy", image="2.8.jpg" )
session.add(product16)
session.commit()

product17 = Product(name="Square Hydraulic Chaffing Dish Type-2", catagory="CD", id="CD-609", size="12 X 13", price=500, polish="Glossy", image="2.9.jpg" )
session.add(product17)
session.commit()

product18 = Product(name="Rectangular Full Glass Top Hydraulic Dish", catagory="CD", id="CD-610", size="18, 20 lt", price=500, polish="Glossy", image="3.1.jpg" )
session.add(product18)
session.commit()

product19 = Product(name="Double Patti Glass Top Hydraulic Dish", catagory="CD", id="CD-611", size="18, 20 lt", price=500, polish="Glossy", image="3.2.jpg" )
session.add(product19)
session.commit()

product20 = Product(name="Single Patti Glass Top Hydraulic Dish", catagory="CD", id="CD-612", size="18, 20 lt", price=500, polish="Glossy", image="3.3.jpg" )
session.add(product20)
session.commit()

product21 = Product(name="Full Glass Top Hydraulic Dish", catagory="CD", id="CD-613", size="18, 20 lt", price=500, polish="Glossy", image="3.4.jpg" )
session.add(product21)
session.commit()

product22 = Product(name="Riser Hydraulic Chaff Dish", catagory="CD", id="CD-614", size="12 X 13", price=500, polish="Glossy", image="3.5.jpg" )
session.add(product22)
session.commit()

product23 = Product(name="Square Glass Top Hydraulic Dish", catagory="CD", id="CD-615", size="18, 20 lt", price=500, polish="Glossy", image="3.6.jpg" )
session.add(product23)
session.commit()

product24 = Product(name="Fish Leg Hydraulic Chaffing Dish", catagory="CD", id="CD-616", size="18 lt", price=500, polish="Glossy", image="4.1.jpg" )
session.add(product24)
session.commit()

product25 = Product(name="Gujrati Handi", catagory="CD", id="CD-617", size="18 lt", price=500, polish="Glossy", image="4.2.jpg" )
session.add(product25)
session.commit()

product26 = Product(name="Gujrati Handi type-2", catagory="CD", id="CD-618", size="18 lt", price=500, polish="Glossy", image="4.3.jpg" )
session.add(product26)
session.commit()

product27 = Product(name="Bridge Handi", catagory="CD", id="CD-619", size="18 lt", price=500, polish="Glossy", image="4.4.jpg" )
session.add(product27)
session.commit()

product28 = Product(name="Pipe Leg Handi", catagory="CD", id="CD-620", size="18 lt", price=500, polish="Glossy", image="4.5.jpg" )
session.add(product28)
session.commit()

product29 = Product(name="Chowki Handi", catagory="CD", id="CD-621", size="18 lt", price=500, polish="Glossy", image="4.6.jpg" )
session.add(product29)
session.commit()

product30 = Product(name="Bridge Handi Type-2", catagory="CD", id="CD-622", size="18 lt", price=500, polish="Glossy", image="4.7.jpg" )
session.add(product30)
session.commit()

product31 = Product(name="Hammered Handi", catagory="CD", id="CD-623", size="18 lt", price=500, polish="Glossy", image="4.8.jpg" )
session.add(product31)
session.commit()

product32 = Product(name="Rectangular Roll Top Dish", catagory="CD", id="CD-624", size="18, 20 lt", price=500, polish="Glossy", image="4.9.jpg" )
session.add(product32)
session.commit()

product33 = Product(name="Square Chaffing Dish", catagory="CD", id="CD-625", size="12 X 13", price=500, polish="Glossy", image="4.10.jpg" )
session.add(product33)
session.commit()

product34 = Product(name="X Rectangular Roll Top", catagory="CD", id="CD-626", size="18, 20 lt", price=500, polish="Glossy", image="4.11.jpg" )
session.add(product34)
session.commit()

product35 = Product(name="Square Hydraulic Chaffing Dish", catagory="CD", id="CD-627", size="12 X 13", price=500, polish="Glossy", image="4.12.jpg" )
session.add(product35)
session.commit()

product36 = Product(name="Fish Leg Round Chaffing Dish", catagory="CD", id="CD-628", size="18 lt", price=500, polish="Glossy", image="6.1.jpg" )
session.add(product36)
session.commit()

product37 = Product(name="Pipe Leg Hydraulic Chaffing Dish", catagory="CD", id="CD-629", size="18 lt", price=500, polish="Glossy", image="6.2.jpg" )
session.add(product37)
session.commit()

product38 = Product(name="Double Patti Hydraulic Chaffing Dish", catagory="CD", id="CD-630", size="18 lt", price=500, polish="Glossy", image="6.3.jpg" )
session.add(product38)
session.commit()

product39 = Product(name="Pipe Leg Circular Dish Type 2", catagory="CD", id="CD-631", size="18 lt", price=500, polish="Glossy", image="6.4.jpg" )
session.add(product39)
session.commit()

product40 = Product(name="Short Leg Circular Dish", catagory="CD", id="CD-632", size="18 lt", price=500, polish="Glossy", image="6.5.jpg" )
session.add(product40)
session.commit()

product41 = Product(name="Fish Leg Round Dish Type 2", catagory="CD", id="CD-633", size="18 lt", price=500, polish="Glossy", image="6.6.jpg" )
session.add(product41)
session.commit()

product42 = Product(name="Fish Leg round Dish Coloured", catagory="CD", id="CD-634", size="18 lt", price=500, polish="Glossy", image="5.1.jpg" )
session.add(product42)
session.commit()

product43 = Product(name="Pipe Leg Top Glass Chaffing Dish", catagory="CD", id="CD-635", size="18 lt", price=500, polish="Glossy", image="5.2.jpg" )
session.add(product43)
session.commit()

product44 = Product(name="Maharaja Chaffing Dish", catagory="CD", id="CD-636", size="18 lt", price=500, polish="Glossy", image="5.3.jpg" )
session.add(product44)
session.commit()

product45 = Product(name="Double Patti Hydraulic Chaffing Dish", catagory="CD", id="CD-637", size="5, 8 lt", price=500, polish="Glossy", image="5.4.jpg" )
session.add(product45)
session.commit()

product46 = Product(name="Plain Tentware", catagory="CD", id="CD-638", size="5, 8 lt", price=500, polish="Glossy", image="5.5.jpg" )
session.add(product46)
session.commit()

product47 = Product(name="Lift Top Chaffing Dish", catagory="CD", id="CD-639", size="5, 8 lt", price=500, polish="Glossy", image="5.6.jpg" )
session.add(product47)
session.commit()

product48 = Product(name="Roll Top Chaffing Dish", catagory="CD", id="CD-640", size="5, 8 lt", price=500, polish="Glossy", image="5.7.jpg" )
session.add(product48)
session.commit()

product49 = Product(name="Gold Hydraulic Chaffing Dish", catagory="CD", id="CD-641", size="5, 8 lt", price=500, polish="Glossy", image="5.8.jpg" )
session.add(product49)
session.commit()

product50 = Product(name="Pipe jug 3", catagory="TW", id="TW-703", size="standard", price=300, polish="Mathar", image="7.3.jpg" )
session.add(product50)
session.commit()

product51 = Product(name="Hammered Kadai", catagory="TW", id="TW-704", size="1, 2, 3", price=500, polish="Glossy", image="7.4.jpg" )
session.add(product51)
session.commit()

product52 = Product(name="Cutlery", catagory="TW", id="TW-705", size="baby, dessert", price=500, polish="Glossy", image="7.5.jpg" )
session.add(product52)
session.commit()

product53 = Product(name="Hammered Copper Kadai", catagory="TW", id="TW-706", size="1, 2, 3", price=500, polish="Glossy", image="7.6.jpg" )
session.add(product53)
session.commit()

product54 = Product(name="Table Barbecue", catagory="TW", id="TW-707", size="standard", price=500, polish="Mat", image="7.7.jpg" )
session.add(product54)
session.commit()

product55 = Product(name="Hammered Copper Balti", catagory="TW", id="TW-708", size="1, 2", price=500, polish="Glossy", image="8.1.jpg" )
session.add(product55)
session.commit()

product56 = Product(name="Hammered Copper Handi", catagory="TW", id="TW-709", size="1, 2, 3", price=500, polish="Glossy", image="8.2.jpg" )
session.add(product56)
session.commit()

product57 = Product(name="Hammered Balti", catagory="TW", id="TW-710", size="1, 2", price=500, polish="Glossy", image="8.3.jpg" )
session.add(product57)
session.commit()

product58 = Product(name="Hammered Handi", catagory="TW", id="TW-711", size="1, 2, 3, 4", price=500, polish="Mathar", image="8.4.jpg" )
session.add(product58)
session.commit()

product59 = Product(name="Serving Tray", catagory="TW", id="TW-712", size="standard", price=500, polish="Glossy", image="8.5.jpg" )
session.add(product59)
session.commit()

product60 = Product(name="Napkin Holder 1", catagory="TW", id="TW-713", size="standard", price=500, polish="Glossy", image="8.6.jpg" )
session.add(product60)
session.commit()

product61 = Product(name="Napkin Holder 2", catagory="TW", id="TW-714", size="standard", price=500, polish="Glossy", image="8.7.jpg" )
session.add(product61)
session.commit()

product62 = Product(name="Bar Tray", catagory="TW", id="TW-715", size="16, 18", price=500, polish="Glossy", image="8.8.jpg" )
session.add(product62)
session.commit()

product63 = Product(name="Snack Warmer", catagory="TW", id="TW-716", size="standard", price=500, polish="Glossy and Mat", image="8.9.jpg" )
session.add(product63)
session.commit()

product64 = Product(name="Top", catagory="HW", id="HW-803", size="12-24", price=500, polish="Glossy", image="9.3.jpg" )
session.add(product64)
session.commit()

product65 = Product(name="Plate", catagory="HW", id="HW-804", size="11, 12", price=500, polish="Glossy", image="9.4.jpg" )
session.add(product65)
session.commit()

product66 = Product(name="Bowls", catagory="HW", id="HW-805", size="5.5-11", price=500, polish="Glossy", image="9.5.jpg" )
session.add(product66)
session.commit()

product67 = Product(name="Sauce Pan", catagory="HW", id="HW-806", size="10-13", price=500, polish="Glossy", image="9.6.jpg" )
session.add(product67)
session.commit()

product68 = Product(name="6 Pan Open Trolley", catagory="TB", id="TB-503", size="standard", price=500, polish="Glossy", image="10.3.jpg" )
session.add(product68)
session.commit()

product69 = Product(name="Square Dustbin", catagory="TB", id="TB-504", size="standard", price=500, polish="Glossy", image="10.4.jpg" )
session.add(product69)
session.commit()

product70 = Product(name="6 Pan Trolley Type-2", catagory="TB", id="TB-505", size="standard", price=500, polish="Glossy", image="10.5.jpg" )
session.add(product70)
session.commit()

product71 = Product(name="Bar Trolley Type-2", catagory="TB", id="TB-506", size="standard", price=500, polish="Glossy", image="10.6.jpg" )
session.add(product71)
session.commit()

product72 = Product(name="Rose Gold Bite to Eat Trolley", catagory="TB", id="TB-507", size="standard", price=500, polish="Glossy", image="12.1.jpg" )
session.add(product72)
session.commit()

product73 = Product(name="Gold Plated Trolley", catagory="TB", id="TB-508", size="standard", price=500, polish="Glossy", image="12.2.jpg" )
session.add(product73)
session.commit()

product74 = Product(name="Water Bottle Trolley", catagory="TB", id="TB-509", size="standard", price=500, polish="Glossy", image="12.3.jpg" )
session.add(product74)
session.commit()

product75 = Product(name="Rose Gold Barbeque Trolley", catagory="TB", id="TB-510", size="standard", price=500, polish="Glossy", image="13.1.jpg" )
session.add(product75)
session.commit()

product76 = Product(name="3 Pan Snack Trolley", catagory="TB", id="TB-511", size="standard", price=500, polish="Glossy", image="13.2.jpg" )
session.add(product76)
session.commit()

product77 = Product(name="Black Titanium Used Plate Trolley", catagory="TB", id="TB-512", size="standard", price=500, polish="Glossy", image="13.3.jpg" )
session.add(product77)
session.commit()

product78 = Product(name="X-Trolley", catagory="TB", id="TB-513", size="standard", price=500, polish="Glossy", image="11.1.jpg" )
session.add(product78)
session.commit()

product79 = Product(name="Covered Dustbin", catagory="TB", id="TB-514", size="standard", price=500, polish="Glossy", image="11.2.jpg" )
session.add(product79)
session.commit()

product80 = Product(name="Long Tub", catagory="TB", id="TB-515", size="22, 24 inch", price=500, polish="Glossy", image="11.3.jpg" )
session.add(product80)
session.commit()

product81 = Product(name="Round Tub", catagory="TB", id="TB-516", size="3, 4, 5, 6", price=500, polish="Glossy", image="11.4.jpg" )
session.add(product81)
session.commit()

product82 = Product(name="Rectangular Tub", catagory="TB", id="TB-517", size="standard", price=500, polish="Glossy", image="11.5.jpg" )
session.add(product82)
session.commit()

product83 = Product(name="X-Table", catagory="TB", id="TB-518", size="standard", price=500, polish="Glossy", image="11.6.jpg" )
session.add(product83)
session.commit()

product84 = Product(name="Long Dustbin", catagory="TB", id="TB-519", size="standard", price=500, polish="Glossy", image="11.7.jpg" )
session.add(product84)
session.commit()

product85 = Product(name="Dosa Counter", catagory="CN", id="CN-903", size="standard", price=500, polish="Mat and Glossy", image="14.3.jpg" )
session.add(product85)
session.commit()

product86 = Product(name="Single Bhatti Counter", catagory="CN", id="CN-904", size="standard", price=500, polish="Mat and Glossy", image="14.4.jpg" )
session.add(product86)
session.commit()

product87 = Product(name="Double Standing Bhatti", catagory="CN", id="CN-905", size="standard", price=500, polish="Mat and Glossy", image="14.5.jpg" )
session.add(product87)
session.commit()

product88 = Product(name="Single Standing Bhatti", catagory="CN", id="CN-906", size="standard", price=500, polish="Mat and Glossy", image="14.6.jpg" )
session.add(product88)
session.commit()

product89 = Product(name="Roti Counter", catagory="CN", id="CN-907", size="standard", price=500, polish="Mat and Glossy", image="15.1.jpg" )
session.add(product89)
session.commit()

product90 = Product(name="Roti Keeper", catagory="CN", id="CN-908", size="standard", price=500, polish="Mat and Glossy", image="15.2.jpg" )
session.add(product90)
session.commit()

product91 = Product(name="Double Bhatti Counter", catagory="CN", id="CN-909", size="standard", price=500, polish="Mat and Glossy", image="15.3.jpg" )
session.add(product91)
session.commit()

product92 = Product(name="Dosa Counter 2", catagory="CN", id="CN-910", size="standard", price=500, polish="Mat and Glossy", image="15.4.jpg" )
session.add(product92)
session.commit()

product93 = Product(name="SS Bhatti", catagory="CN", id="CN-911", size="12X12, 14X14, 16X16", price=500, polish="Mat and Glossy", image="15.5.jpg" )
session.add(product93)
session.commit()

product94 = Product(name="Double Bhatti", catagory="CN", id="CN-912", size="standard", price=500, polish="Mat and Glossy", image="15.6.jpg" )
session.add(product94)
session.commit()



best1 = Bestseller(name="Bar Trolley", product_id="TB-501")
session.add(best1)
session.commit()

best2 = Bestseller(name="Dosa Counter", product_id="CN-902")
session.add(best2)
session.commit()

best3 = Bestseller(name="Balti", product_id="HW-801")
session.add(best3)
session.commit()

best4 = Bestseller(name="Pipe jug", product_id="TW-701")
session.add(best4)
session.commit()

ware1 = Ware(name="CHAFING DISHES", id="CD", image="https://c1.staticflickr.com/5/4243/34088506774_ee676ec6d2_o.png")
session.add(ware1)
session.commit()

ware2 = Ware(name="TABLEWARE", id="TW", image="https://c1.staticflickr.com/5/4243/34088506774_ee676ec6d2_o.png")
session.add(ware2)
session.commit()

ware3 = Ware(name="HOUSEWARE", id="HW", image="https://c1.staticflickr.com/5/4243/34088506774_ee676ec6d2_o.png")
session.add(ware3)
session.commit()

ware4 = Ware(name="COUNTERS", id="CN", image="https://c1.staticflickr.com/5/4243/34088506774_ee676ec6d2_o.png")
session.add(ware4)
session.commit()

ware5 = Ware(name="TROLLEYS AND BINS", id="TB", image="https://c1.staticflickr.com/5/4243/34088506774_ee676ec6d2_o.png")
session.add(ware5)
session.commit()

catalog1 = Catalog(image="Prem_Products_Title_Front.jpg")
session.add(catalog1)
session.commit()

catalog2 = Catalog(image="1.jpg")
session.add(catalog2)
session.commit()

catalog3 = Catalog(image="2.jpg")
session.add(catalog3)
session.commit()

catalog4 = Catalog(image="3.jpg")
session.add(catalog4)
session.commit()

catalog5 = Catalog(image="4.jpg")
session.add(catalog5)
session.commit()

catalog6 = Catalog(image="5.jpg")
session.add(catalog6)
session.commit()

catalog7 = Catalog(image="6.jpg")
session.add(catalog7)
session.commit()

catalog8 = Catalog(image="7.jpg")
session.add(catalog8)
session.commit()

catalog9 = Catalog(image="8.jpg")
session.add(catalog9)
session.commit()

catalog10 = Catalog(image="9.jpg")
session.add(catalog10)
session.commit()

catalog11 = Catalog(image="10.jpg")
session.add(catalog11)
session.commit()

catalog12 = Catalog(image="11.jpg")
session.add(catalog12)
session.commit()

catalog13 = Catalog(image="12.jpg")
session.add(catalog13)
session.commit()

catalog14 = Catalog(image="13.jpg")
session.add(catalog14)
session.commit()

catalog15 = Catalog(image="14.jpg")
session.add(catalog15)
session.commit()

catalog16 = Catalog(image="15.jpg")
session.add(catalog16)
session.commit()

catalog17 = Catalog(image="Prem_Products_Title_Back.jpg")
session.add(catalog17)
session.commit()



print "added menu items!"
