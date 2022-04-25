# GPUTracker
## Functionality
Users connect to site and are greeted by a generic web page. From there, users can create an account or log in to an existing account. Once a user has logged in, they will see a new web page. On this page, the user can enter products they would like to track the price of or view products they are already tracking. If a user adds a new product to track, that item will be permanently added to their profile until they manually delete it.

## Structure
### Web Scraper (Python)
	- Regularly checks and upates prices gotten from newegg.com

### mySQL Database
	- List of products user is tracking.
	- Prices of tracked products.
	- User login details.

### WebUI (Angular)
	- Generic home page that user can log in to or create a new account
	- User page where they can see their tracked products or track new ones
