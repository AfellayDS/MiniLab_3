# Laboratory work No. 3 (I option)
Student: Filippov Denis (group 5030102/10401).
## Launching the application
1. Clone the repository
2. Create and activate a virtual environment for the project
3. Install dependencies using the command
	```bash
	pip install -r requirements.txt
	```
4. Launch the application using the command
	```bash
	streamlit run main.py
	```
## Program description
The application provides a software interface for working with the information and statistical server of the Moscow Exchange. The following types of information are available within the interface: static data on markets (trading modes and their groups, financial instruments and their descriptions), data for plotting charts (“candles”), quotes, dividends, various metadata. Documentation of implemented queries is available in [Postman](https://elements.getpostman.com/redirect?entityId=31837212-c0e4d8ef-f3f2-4594-9f48-0d012e77395f&entityType=collection).

A web interface is available for entering and outputting information. The user needs to maintain the company ticker (SBER, GAZP, PHOR, YNDX) and the time interval within which historical data should be displayed. After this, the application will create a dashboard that contains information about the company's historical quotes and paid dividends.
