# PC Geeks
## A PC Part Trading Website
PC Geeks is a website strictly for people to sell and buy pc parts. When we created this site, we wanted to make a platform that is easy to navigate, less convoluted than CraigsList, and a channel for users to cummunicate directly in-app.

We used Angular2JS for the frontend and Django for the backend. Angular2 allows for the website to be reactive
and fast. Parts are categorized, and allow the poster to upload images of their product.
Google maps implementation to assist in post location and seller location.
Initially, our goal was to make a platform that can simply to navigate, less complicated than
Craigslist, and a built-in messaging service where a purchaser can directly keep in touch with the seller.
Due to the nature of users, we also had the opportunity to implement a reporting feature for posts that
are misleading or vulgar. Additionally, the reporting feature sends a message via email towards the
administrator. We also created a rating feature where a user can be rated on a scale of 1 to 5 based on
their performance and how they manage a transaction.
Sale postings can include several attributes: images, location (google maps), quality,
manufacturer, category, and a description. Each post can be quickly and easily searched up and filtered
out using the built in filter feature that can filter posts without reloading the page. 

## List of available similar services:
Craigslist - Craigslist is a very large and popular website that anyone can post anything they
desire. Buying and selling products are sometimes hard to do since they are many scattered categories to
choose from. I would end up with posts that are not useful to me. Messaging the buyer/seller requires
another source of communication such as cell phone or email and not via the website.
Our web application “PC Geeks” avoids this by making sure each item is under specific
categories so there will be no overlaps. If a user wants to search up a name of a video card, only the same
category of video card will appear. We also have a messaging system that allows the buyer to directly
contact the seller. This way transactions can happen a lot quicker.

## Future goal of our project:
Future work I might want to see be done on this project is to incorporate components that
analyze the costs of the posts. On the off chance that you see a section that is available to be purchased
at a range of prices, I need to see the costs of comparable parts. At that point I can think about various
posts in view of the cost for quality. 
Additionally, I need to add highlights where it snatches the costs from retailers to contrast it with
the costs taken by users. This will enable purchasers and dealers to get a feeling of the business
transaction for a thing and change the second-hand cost appropriately.
Other features include tracking how many specific items are for sale currently and automatic
notification system for when a specific item hits a certain price. If one is overeager and confident in
security practices, perhaps online money would be good to have implemented.


### To run the web app:
1. Use `vagrant up` to launch the VM.
2. Access `localhost:4200` on your host machine.
3. Refresh the server using the `build.sh` script.


### Features
#### Posting
PC Geeks provide a structured posting format. The seller must select the type (video card, CPU, etc..) and manufacturer of the item they are selling from a drop-down menu. Seller must also provide their preferred location of transaction which will be shown to other viewers.

#### Messaging
When a user see an item they are interested in buying/selling, they can go inside the detail page of the posting and send the other party a message. All parties are anonymous in a conversation to ensure security.

#### Rating
Inside every sales detail page, users can give feedback to the the post owner. These anonymous ratings can be seen by other users.

#### Reporting
Due to the nature of people, we also created a reporting feature to report posts that are inappropriate or misleading. The reporting feature sends an email to a admin account.

### Admin Email info:
Email: pcgeeks470@gmail.com
Password: ytrewq123

### Test Users info:
User name: tester1
Password: password

User name: tester2
Password: password

User name: tester3
Password: password
