# Web-Scrapping

<p align="center">
  <img src="https://user-images.githubusercontent.com/65192837/213873054-0c65f672-fb14-462e-af80-cc7401146f9d.png" alt="Sublime's custom image"/>
</p>

## Introduction

**Any field of study or area of personal interest can benefit greatly from the enormous amount of data on the Internet.” Given the volume, variety, velocity, and veracity of Big Data available on the Web, collection and organization of this data can hardly be done manually by individual researchers or even large research teams. Because of that, researchers often resort to various technologies and tools to automate some aspects of data collection and organization” ( Krotov, V., & Silva, L. (2018).** 

Web scraping is used to collect large amounts of data from websites, fast. It can be used to extract information from a website, such as product names, prices, and reviews, and then save that information to a file or database. It can also be used to track changes to a website, such as changes to prices or product availability. Additionally, it can be used to automate tasks, such as logging into a website, filling out forms, and clicking buttons.

In general, we refer Information gathering from the Internet as web scraping. Usually when we say web scrapping we typically mean an automated procedure. However, web scraping is not always legal, as some websites may have terms of service that prohibit scraping, or the website may have technical measures in place to prevent scraping. Therefore it is important to check a website's terms of service and to be respectful of the website's resources and servers when scraping or conduct our own research and confirm that we are not infringing on any Terms of Service.

The Web has evolved naturally from a variety of sources. It incorporates a wide range of technologies, patterns, and personalities and is still expanding today.Therefore, the Internet now a days is a complicated mess. Due to this, a few difficulties arise when we opt for web scrapping:

> ### Variety
>
> - Each website is different from other website in terms of structure and backend code, also, it varies as per the domain of the business and the purpose it serves to the end customers. 
>  - While there are recurring general structures, each website is different and will require individualized attention if we want to extract the necessary information.
        
> ### Durability
>
> - Websites are constantly evolving. We've created a web scraper from the scratch that automatically extracts the information we need from Booking.com. Our script runs without a hitch at this point of instance. 
> - But may be in near future, if we run the same script, we may have multiple errors in parsing the data from web as the structure of the website might change or migrates to a newer version.

## Context and dataset description

There are many factors that influence the price of property for rent. Some of these factors include the location of the property, the size of the property, the condition of the property, the amenities that are available at the property, and the rental history of the property. Booking a hotel online can be a great way to save money on your trip. Many hotels offer online booking services that allow us to make reservations without having to speak to a live person. We can also find great deals on hotels by using online travel agencies. When booking hotels online, there are a few common issues that can arise. Some of the most common problems include being unable to locate the hotel we seek, being charged for services we did not use, dealing with difficult customer service, being unable to make a reservation, and being unable to obtain a refund for a reservation. At the cost of this issues, the price of a property can varies. Some of the online platform utilise these constraints to formulate a customised pricing strategy to attract customers to book the properties using their platform. The Objective of this project is to determine the factors that can influence the price for one night stay in Paris using data gathering utilizing web scrapping an online hotel booking platform – Booking.com.

Booking.com is a small Dutch start-up which is one of the top global providers of online travel services. The goal is to make it simpler for everyone to travel. It connects millions of travellers for an unforgettable experiences, a wide range of transportation options, and amazing places to stay, including homes, hotels, and many more, by investing in technology that removes the friction from travel.

To extract the available data over the internet, we need web scraping if we want to collect those data effectively. Selenium, Requests and Beautiful Soup are effective tools for the job in Python. For the current task we are scrapping information regarding available property for one night stay in Paris on Booking.com.
Using the scrapper, we are extracting information about the property name, preferred plus status, number of stars, address, proximity to the city center, availability of a metro stop nearby, reviews from booking.com and user feedback, room, and bed types, whether the property is travel sustainable or not, rating, price per night, whether breakfast is included, and whether prepayment is required or not.

- property_name
- preferred_plus_property
- property_stars
- property_address
- dist_from_center
- metro_access
- booking_reviews
- user_reviews
- room_type
- bed_type
- sus_property_type
- property_rating
- price_per_night
- breakfast_included
- free_cancellation_no_prepayment

## Approach

In the project, we are using a scrapper which automatically search for the available properties for stay in Paris at the present and navigate through each page and scrap all the required information and feed it to relevant columns. Following which we create a pandas data frame for exploratory data analysis and extract the data in excel and csv format file to have a backup copy of the data.

## Challenges

During the process, we can observe that the data extracted needs to be cleaned and converted into relevant format in order to work on exploratory data analysis. Further, there are multiple elements which can introduce data inaccuracy due to the additional elements available in the given container section of the product such as discounted price. Also, the additional banner appearing on the windows/screen such as user consent for storing cookies, sign in popup, and interaction with calendar element can break the existing code during the compilation process. To extract the "proper" information, we must understand the data and its context. Without domain expertise, we risk giving out inaccurate and misleading information.

## Conclusion

Property rating, user reviews, distance from the city center, metro accessibility, free cancellation, and complimentary breakfast option can all have a significant impact on the price of a one-night stay. Using these criteria, hotels can vary their prices for one night stay.
