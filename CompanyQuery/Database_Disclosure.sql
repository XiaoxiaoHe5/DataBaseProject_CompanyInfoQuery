CREATE DATABASE Disclosure DEFAULT CHARACTER SET utf8mb4;
USE Disclosure;

create table Stock  -- 个股
(Stockcode varchar(20) primary key,
lastupdateyear varchar(20),
Sharesreferredtoas varchar(255),
FullnameofthecompanyinChinese varchar(255),
ThefullnameofthecompanyinEnglish varchar(255),
CSRCindustryclassification varchar(255),
GICSindustryclassification varchar(255),
Placeofincorporation varchar(255),
Stockexchange varchar(255),
Smeboardmarking varchar(255),
Transactionstatus varchar(255)
);

create table StockChange  -- 个股更改
(Recordnumber varchar(255) primary key,
Stockcode varchar(20),
Changetheobject varchar(255),
Changethedate varchar(255),
Changethevaluebefore varchar(255),
Thechangedvalue varchar(255),
foreign key(Stockcode)references Stock(Stockcode)
);

create table Conference  -- 会议
(Stockcode varchar(20),
Theannual varchar(20),
Number0 varchar(255),
Attendrate0 varchar(255),
Number1 varchar(255),
Attendrate1 varchar(255),
Number2 varchar(255),
Attendrate2 varchar(255),
Thenumberofboardmeetingsheldduringtheyear varchar(255),
Numberofboardmeetingsheldbycommunicationduringtheyear varchar(255),
Numberofannualmeetingsoftheboardofsupervisors varchar(255),
Auditcommittee varchar(255),
Compensationandappraisalcommittee varchar(255),
Strategycommittee varchar(255),
Nominatingcommittee varchar(255),
Thetotalnumberofmeetingsoftheannualmeeting varchar(255),
primary key(Stockcode,Theannual)
);

create table Finance1  -- 财务(表1) 
(Stockcode varchar(20),
Theannual varchar(20),
Dateofpublicationoffinancialreport text,
Operatingincome text,
Netprofit text,
Totalassets text,
Totalownersequity text,
Netnonoperatingincome text,
Networkingcapital text,
Basicearningspershare text,
Dilutedearningspershare text,
Earningspershare_dilutedoperatingprofit text,
Earningspershare_dilutednetincome text,
Netassetpershare text,
Operatingincomepershare text,
Returnonequity_operatingprofit text,
Returnonequity_netprofit text,
Returnonassets text,
Netprofitmargin text,
Growthrateofnetassets text,
Growthrateoftotalassets text,
Revenuegrowthrate text,
Operatingprofitgrowthrate text,
Aftertaxprofitgrowthrate text,
Currentratio text,
Quickratio text,
Inventorycurrentliabilityratio text,
Cashflowdebtratio text,
Capitaladequacyratio text,
Cashtodebtratio text,
Debtcapitalratio text,
Debttoassetratio text,
Inventoryturnover text,
Accountsreceivableturnover text,
Turnoverofcurrentassets text,
Assetturnover text,
Turnoveroffixedassets text,
Inventoryperiod text,
Receivablecollectionperiod text,
Peratio text,
pricetobook text,
Pricetosalesratio text,
TobinQ text,
Adjustlastyearsoperatingincome text,
Adjusttheoperatingincomeoftheyearbeforelast text,
Adjustednetprofitlastyear text,
Adjustthenetprofittheyearbefore text,
Adjusttotalassetsforlastyear text,
Adjustthetotalassetsoftheyearbeforelast text,
Adjustlastyearsequity text,
Adjusttheequityofthepreviousyear text,
Adjustedlastyearsbasicearningspershare text,
Adjustedbasicearningspersharefortheyearbeforelast text,
Adjustthenetassetspersharelastyear text,
Adjustthenetassetspersharetheyearbeforelast text,
Adjustednetcashflowforthepreviousyear text,
Adjustednetcashflowfortheyearbeforelast text,
Adjustedlastyearsacrosstheboarddilutedreturnonequity text,
Adjustedtheyearbeforetheoveralldilutedreturnonequity text,
Adjustedlastyearsweightedaveragereturnonequity text,
Adjustedwareturnonequityfortheyearbeforelast text,
Accountingfirm text,
Signatureaccountant text,
Theauditfee text,
Theauditopinion text,
Monetaryfund text,
Transactionalfinancialassets text,
Shortterminvestmentdepreciationreserve text,
Netshortterminvestment text,
Notesreceivable text,
Dividendsreceivable text,
Interestreceivable text,
Accountsreceivable text,
Otherreceivables text,
Provisionforbaddebt text,
Netreceivables text,
prepayments text,
Exportrebatereceivable text,
Allowancereceivable text,
inventory text,
Engineeringconstruction text,
Depletingbiologicalassets text,
Provisionforfallingstockprices text,
Netinventory text,
Prepaidexpenses text,
Netlossoncurrentassetstobetreated text,
Noncurrentassetsmaturingwithinoneyear text,
Othercurrentassets text,
Premiumsreceivable text,
Reinsurancecontractreservereceivable text,
Buyresalefinancialassets text,
Derivativefinancialassets text,
Paymenthasnotbeensettledyet text,
Engineeringcontractpaymentsreceivable text,
Settlementprovisions text,
Lendingmoney text,
Accountreceivablefactoring text,
Holdingilliquidassetsforsale text,
Hedgeditem text,
Hedginginstrument text,
Internaldebits text,
Totalcurrentassets text,
Longtermequityinvestment text,
Longtermreceivables text,
Equityinvestmentbalance text,
Splitcirculationofshares text,
Availableforsalefinancialassets text,
Holdtomaturityinvestment text,
Otherlongterminvestments text,
Longterminvestment text,
Totallongterminvestment text,
Impairmentprovisionforlongterminvestments text,
Netlongterminvestment text,
Mergespreads text,
Fixedassets text,
Accumulateddepreciation text,
Netfixedassets text,
Provisionforimpairmentoffixedassets text,
Netfixedasset text,
Engineeringmaterials text,
Projectsunderconstruction text,
Advancepaymentforprojectandprojectmaterials text,
Liquidationoffixedassets text,
Netlossonfixedassetstobetreated text,
Operationleasingfixedassetsimprovement text,
primary key(Stockcode,Theannual)
);


create table Finance2  -- 财务(表2) 
(Stockcode varchar(20),
Theannual varchar(20),
Totalfixedassets text,
Intangibleassets text,
Deferredassets text,
Organizationexpenses text,
Longtermdeferredexpenses text,
Othernoncurrentassets text,
Investmentrealestate text,
Productivebiologicalassets text,
Publicwelfarebiologicalassets text,
Oilandgasassets text,
Liquidationofoilandgasassets text,
Depletionofoilandgasassets text,
Provisionforimpairmentofoilandgasassets text,
Bookvalueofoilandgasassets text,
goodwill text,
Agentbuysandsellssecurities text,
Thedevelopmentofspending text,
Entrustedloans text,
Financeleasereceivables text,
Issueloansandadvances text,
Deferredincometaxassets text,
Totalnoncurrentassets text,
Shorttermborrowing text,
Notespayable text,
Accountspayable text,
Advancepayment text,
Engineeringsettlement text,
Consignmentsalesofgoods text,
Employeepaypayable text,
Benefitspayable text,
Dividendspayable text,
Payabletaxes text,
Otheramountspayable text,
Otherpayables text,
Accruedexpenses text,
Noncurrentliabilitiesduewithinoneyear text,
Othercurrentliabilities text,
Estimateddebts text,
Futuresriskreserve text,
TakedepositsanddepositwithotherBanks text,
Transactionalfinancialliabilities text,
Sellingrepurchaseoffinancialassets text,
Derivativefinancialliability text,
Commissionsandcommissionspayable text,
Interestpayable text,
Bankallocationforaccountreceivablefactoring text,
Accountspayablebyreinsurance text,
Theoutstandingamounthasbeensettled text,
Workscontractpayable text,
Shorttermbondspayable text,
Domesticclearing text,
Internationalclearing text,
Deferredrevenue text,
Nocivilaviationinfrastructurefund text,
Totalcurrentliabilities text,
Longtermborrowing text,
Bondspayable text,
Longtermpayables text,
Othernoncurrentliabilities text,
Housingaccumulationfund text,
Specialpayables text,
Insurancecontractreserve text,
Financeleasepayable text,
Agencybusinessliabilities text,
Totalnoncurrentliabilities text,
Deferredincometaxliabilities text,
Totalliabilities text,
Minorityequity text,
Paidupcapital_orsharecapital text,
Capitalreserves text,
Surplusreserves text,
Thecommunitychest text,
Statutorysurplusreserve text,
Anysurplusreserve text,
Foreigncurrencystatementtranslationbalance text,
Undistributedprofits_assetsandliabilities text,
Treasurystock text,
Generalriskpreparation text,
Thisyearsprofits text,
Proposeddistributionofcommonstockdividends text,
Totalownershipequityattributabletotheparentcompany text,
Theaccumulatedlossesofthesubsidiaryhavenotbeencovered text,
Unrecognisedinvestmentlosses_assetsandliabilities text,
Totalliabilitiesandequity text,
Grossrevenue text,
Otherbusinessincome text,
Exportrevenue text,
Interestincome text,
Thepremiumhasbeenmade text,
Feesandcommission text,
Rentalincome text,
Discountsandallowances text,
Netincomefrommainbusiness text,
Totaloperatingcost text,
Operatingcost text,
Otherbusinesscosts text,
Exportbusinesscost text,
Researchanddevelopmentcosts text,
Feesforthesame text,
Theinterestpayments text,
Feesandcommissions text,
Surrendergold text,
Netcompensation text,
Drawthenetamountoftheinsurancecontractreserve text,
Businesstaxandsurcharge text,
Costofsales text,
Managementfees text,
Financecharges text,
Impairmentloss text,
Gainsfromchangesinfairvalue_markedwithforlosses text,
Returnoninvestment text,
Incomefrominvestmentsinjointventuresandjointventures text,
Otherbusinessprofit text,
Netincomefromotherbusinesses_netlossmarkedwith text,
Futuresprofitandloss text,
Exchangegain_lossmarkedwith text,
Operatingprofit text,
Nonoperatingincome text,
Nonoperatingexpenses text,
Lossondisposalofnoncurrentassets text,
Incometaxexpense text,
primary key(Stockcode,Theannual)
);

create table Shareholder  -- 股东持股
(Stockcode varchar(20),
Theannual varchar(20),
NameofShareholder varchar(255),
Shareholdratio text,
numberofsharehold text,
primary key(Stockcode,Theannual,NameofShareholder)
);

create table Transact  -- 交易
(Transactionno varchar(255) primary key,
Stockcode varchar(20),
Theannual varchar(20),
Theannouncementdate varchar(255),
Nameoftheaffiliatedpartyenterprise varchar(255),
Relatedpartycontrolrelationship varchar(255),
Relationshipbetweenrelatedpartiesandlistedcompanies varchar(255),
Sourceofinformation varchar(255),
currency varchar(255),
Monetaryunit varchar(255),
Transactionamountinvolved varchar(255),
Transactiontype varchar(255)
);

create table LawCase  -- 涉案
(Caseno varchar(255) primary key,
Stockcode varchar(1000),
Theannouncementdate varchar(1000),
Inthecaseoftype varchar(1000),
Thecompanyspositioninthecase varchar(1000),
Thecauseofaction varchar(3000),
Theamountofmoneyinvolvedinthecase varchar(1000),
Decisionsituation varchar(1000),
Theimplementationof varchar(3000),
currency varchar(1000)
);

USE Disclosure;

load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Stock.csv' into table Stock
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\r\n';

load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Conference.csv' into table Conference
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\r\n';

load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Finance1.csv' into table Finance1
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\r\n';

load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Finance2.csv' into table Finance2
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\r\n';

load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Shareholder.csv' into table Shareholder
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\r\n';

load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/Transact.csv' into table Transact
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\r\n';

load data infile 'C:/ProgramData/MySQL/MySQL Server 8.0/Uploads/LawCase.csv' into table LawCase
fields terminated by ',' 
optionally enclosed by '"' 
escaped by '"' 
lines terminated by '\r\n';
