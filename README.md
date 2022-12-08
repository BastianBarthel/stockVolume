# stockVolume
A Python script for the software Origin by OriginLab. Shows the trade volume of a stock for the last 100 days and plots a line diagram from it.
<br />
### Instructions
<br />
Get you free API key from (https://www.alphavantage.co) and set as constant STOCK_API_KEY in stockVolume.py
<br />
Make sure the request package is installed in Origin. If you create an app using this script, use the following code as a pre installation LabTalk script to do this automatically: if (Python.chk("requests") > 1) (type -b "The required Python module «requests» is not installed properly", break 1;);
<br />
Use the following LabTalk code to run this as an app (needs to be in the app directory): strFile$=%@AstockVolume.py;run -pyf %(strFile$)
<br />
Use the following code to start from the script window: run -pyf "stockVolume.py"
