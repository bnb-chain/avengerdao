# AvengerDAO - Call for Proposals

## Challenge 1: Identify New Smart Contracts with TVL > $500K dApps on Timely Manner

Description:

- Ideally identify the newly deployed contracts from TVL > 500K dApps should be automatically detected.

  - If not possible, need to setup a process to ensure:

  	- The top-level/core projects should inform the techops & security team while they deploy/update any important contract or add any new critical features. 

    - Too many incidents have occurred due to lack of auditing against those new contracts/functions.

## Challenge 2: Obtain dApps Lists with TVL > $200K

- Complete project list on BNB Chain which TVL is greater than $200k as possible

- Project’s website, twitter and TVL is required at least 

- A complete address list associated with the project is recommended


## Challenge 3: Threat Intelligence on new deployed dApps

-  Project/address list on BNB Chain which TVL is greater than $50k and not listed in well-known website such as Defillama/BSCProject
   -  These projects in shadow are most likely to be malicious, and users will conduct security due diligence on them with high priority.
   -  Daily updates are better. 

-  Project/address list on BNB Chain which active users are newly expanding rapidly but not well-known.
   -  Try to flag those malicious projects in this time window before they are impacted enough.
   -  Daily updates are better. 

-  Project/address list on BNB Chain which newly drawing most attention at social media channel
   -  keep monitoring these projects as well.
   -  Daily updates are better. 

## Challenge 4: Security Analytics Database

- Assets database that can tell us the assets(include but not limit to native coin, valuable tokens, liquidity pool, NFTs) hold by an arbitrary address on BNB Chain denominated in US dollars. 
  - Databases should be updated in daily manner at least(hourly update is preferred), querying with SQLlike syntax if preferred.
  - Identify most emerging valuable contracts on BNB Chain to assess them in early time window.
- Token data. 
  - token related data such as TVL, markets and ICO
  - Coinmarketcap is preferred source.
- Verified contracts data
  - The completed daily updated verified contracts data on BNB Chain. 
- Funds flow database that can tell us a group address that has closely funded relations with each other. 
  - API or WebUI
  - Daily updated
  - Leverage this data to clustering malicious family and warn the community in early stage

