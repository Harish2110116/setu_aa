Niti.AI | Backend | AA Integration
Problem
We would like you to build an end-to-end demo using the SETU Account Aggregator API where:

You establish a consent handshake (create and approve)
You create a data session
You fetch sample data 

You will be using the SETU AA sandbox environment (setup info is below). Their docs are here. 
Setu Sandbox Setup
We have created a test FIU account in the sandbox environment (“bridge”) of the AA, Setu. You will be handshaking with their API using the client_id and client_secret to complete consent and fetch the information of a user. 

See the quick start guide here and use Postman setup to make the calls. 

Authentication keys
These keys have to be used for authenticating API calls between your systems and Setu AA
client_id
255d0b6c-492d-44cf-8581-e9494c7b0914 (select text to view credentials)
client_secret
9c2fc756-3d17-46d6-b28d-be4d71953e83 (select text to view credentials)
Deadline & Deliverables
Our expectation is that you're spending less than 4 hours on the problem. Hence you have one day to complete and submit your solution.

Video Intro
Send us a brief video (use Loom or equivalent) (less than 2 mins) about
A time you created a goal and achieved it.
Something you’ve accomplished that you are proud of.

Demo
Typically you will have a bunch of Postman calls or a program (any language) that makes the API calls and performs the consent API handshake and the subsequent data session calls. You can use the same Loom video to share an end-to-end demo and explain your code briefly (2mins). Ensure that you have given view access on the video. 

Evaluation criteria
We are looking for the following:
Did you understand the end-to-end AA framework?
Were you able to follow the How-To Guides from Setu?
Were you able to make a successful API request / response handshake?
Were you able to complete any end-to-end data access flow?
Submission
Please make your submission using the following form: https://forms.gle/D5MYgLv99oFzLFAC6 

Final Notes
See the Problem and Evaluation criteria and understand what is expected. Use your judgment wherever you are stuck to unblock yourself. 

We hope that working on this problem also gives you a peek into innovations happening in the FinTech area in India. You can be a part of that journey with Niti.AI.

Good luck !
FAQs
Do I need to use my mobile number?
Yes. You will get an OTP to your number.
Do I need to share my bank account data? 
No, when you get the list of bank accounts in the handshake, search for a test bank name (you’ll find it) and use it which will give you the test data sets.
How should I present my work?
See the evaluation criteria above. In your video walkthrough highlight what you have done crisply in <2mins.
How long should this take?
Even if you are brand new to the topic of Account Aggregators, you should be able to complete the assignment in 4 hours. If you are unfamiliar with this space, we would encourage you to learn more about the India Stack as India is doing cutting-edge innovation in the fintech space. Also checkout iSpirt.

Appendix 1 - Account Aggregators Overview
Banks offer loans by reviewing the customer’s financial data -- How much do they earn? ; What is their average bank balance and transactions for the last year? ; Do they have deposits and other investments? What is their credit score from CIBIL? etc. Collecting all this information as well verifying the authenticity of the information is difficult and time consuming. The process also forces the customers to share a lot more information than necessary, and do so in unsecure channels (Whatsapp, Emails) exposing their sensitive information and making them vulnerable to data leaks. 

India Stack is changing this via Account Aggregators. Account Aggregators (AA) are non-banking financial companies, licensed by RBI, that act like a bridge, to deliver data from Financial Information Providers or FIPs (entities that hold a customer’s data, such as the tax department and banks) that hold your personal or corporate financial data to Financial Information Users or FIUs (entities that request customer data such as investment firms and other organizations who offer financial products and services) that are providing financial services to you. The purpose of an AA is not to sell, see or store financial information. They only collect and transmit it, securely and after gaining consent from the customer.

Account Aggregators solve the central issue of financial data collection and submission. They also ensure, for the very first time, that customer data remains private and protected. It is for these reasons account aggregators take a customer-first approach, i.e., they put the customer at the center.

For more info on Account Aggregators see here. (Sahamati is the organization formed to promote and strengthen the Account Aggregator ecosystem in India.)

