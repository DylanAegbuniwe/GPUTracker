# GPUTracker
## Functionality
Users connect to site and are greeted by a generic web page. From there, users can create an account or log in to an existing account. Once a user has logged in, they will see a new web page. On this page, the user can enter products they would like to track the price of or view products they are already tracking. If a user adds a new product to track, that item will be permanently added to their profile until they manually delete it.

## Structure
Diagram of structure can be found [here](https://miro.com/app/board/uXjVO8TlMfU=/?share_link_id=227755587270)
### Web Scraper (Python)
- Regularly checks and updates prices from newegg.com

### Database (mySQL)
Diagram of database can be found [here](https://drawsql.app/csc468/diagrams/csc468)
- List of products user is tracking
- Prices of tracked products
- User login details

### WebUI (JavaScript/CSS/HTML/PHP)
- Home page that user can log in to or create a new account
- User page where they can see their tracked products or track new ones
