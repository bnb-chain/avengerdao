# BNB Chain - Web3 Security Framework

### Decentralized Finance Practices Checklist

Classification: **Restricted**

**Stage: Publication stage (60)**

**Introduction**:

The Web3 Security Framework Initiative is a collaborative effort to promote the adoption of best practices in web3 security. The initiative aims to minimize the risks associated with security vulnerabilities and hacks, which have become increasingly prevalent in the web3 space. Moreover, projects that demonstrate full compliance with our rigorous guidelines will earn an on-chain certificate recognized by all the AvengerDAO members on the BNB Chain ecosystem.

This document serves as a comprehensive checklist of the critical elements surrounding the secure development of DeFi decentralized applications.

<table>
    <thead>
        <tr>
            <th>Item ID</th>
            <th>Security Check</th>
            <th>Criticality</th>
            <th>Is Project Compliant?</th>
            <th>Comments</th>
        </tr>
    </thead>
    <tbody>
<!-- General -->
<tr>
    <td><strong>1</strong></td>
    <td><strong>General</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>1.1</td>
    <td>Check to ensure the decentralized application (Dapp) doesn't mistakenly believe that users can only send tokens via its smart contract functions. Tokens can alternatively be sent using the token smart contract transfer function or through a self-destruct mechanism. For example, if a contract's parameter relies only on token balance, this could be manipulated by directly sending tokens to the contract via the transfer function.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>1.2</td>
    <td>Ensure that the logic for deposits is separate from the reward calculation to prevent reserves from affecting the calculation. For instance, developers should use two independent variables to keep deposit shares distinct from reward computations.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>1.3</td>
    <td>Certify there are clearly defined procedures and mechanisms to pause the contracts in case of the detection of a compromised dependency such as oracles. 
    The reasons for contract pausing must be explicitly stated in the procedures. These reasons could range from technical glitches to legal issues or financial problems. Contingency plans should be stated as well, which include Resource Management, Risk Management and Recovery Plan.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>2</strong></td>
    <td><strong>Oracle based services</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><strong>2.1</strong></td>
    <td><strong>Spot price manipulation</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>2.1.1</td>
    <td>In the case of utilizing an on-chain price calculation method, ensure that the price of an asset can't be tampered within the same transaction, like manipulating the original data through flash loans. One mitigation technique is to fetch the on-chain price from a past block, which can help defend against flash loan price manipulation attempts. It's also recommended to derive data from high-liquidity sources from a trustworthy Decentralized Exchange (DEX).</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>2.1.2</td>
    <td>Ensure the on-chain price calculation does not rely on sources with low liquidity, such as limited liquidity pools.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>2.1.3</td>
    <td>Certify the usage of a secure calculation mechanism such as time-weighted average prices.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>2.2</strong></td>
    <td><strong>Centralized Oracles</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>2.2.1</td>
    <td>Entrusting centralized entities with the responsibility of feeding data to smart contracts is risky. Only rely on such service as last resort. In such cases, important due diligence can be done such as: Certify the entity's reputation and data correctness.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>2.2.2</td>
    <td>Verify there is not usage of external data being used without proper verification.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>2.2.3</td>
    <td>Ensure that the centralized party isn't incentivized to supply altered data to the data source. One effective method involves reviewing the historical behavior of the specific centralized party and assessing the likelihood of such an event occurring.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>2.3</strong></td>
    <td><strong>Off-chain Oracles</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>2.3.1</td>
    <td>Such oracles should ensure the aggregation of off-chain data and validate them prior to pushing them on-chain. Such services rely on regular web2 infrastructure and before using their services, it is important to certify they are secure against any vulnerability described in the OWASP vulnerability catalog and that they follow Coding Secure Guidelines.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>2.4</strong></td>
    <td><strong>On-chain Oracles</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>2.4.1</td>
    <td>Ensure the on-chain oracle solution uses a community-driven dispute mechanism, pre-commit, or any feedback mechanism that enables a second layer validation prior to pushing data on-chain.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<!-- Lending Pools -->
<tr>
    <td><strong>3</strong></td>
    <td><strong>Lending Pools</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>3.1</td>
    <td>Ensure only a specific function in the lender smart contract is called when performing a flash loan.</td>
    <td>Medium</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>3.2</td>
    <td>Prevent reentrancy attacks in the flash loan function. Solutions include implementing checks, effects, and interactions principles or Reentrancy solutions across the smart contract’s state changing functions.</td>
    <td>Critical</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>3.3</td>
    <td>Certify the mechanism calculating the number of tokens before and after the loans is not vulnerable. This includes ensuring the token used is whitelisted such as only the project’s token and ensuring the token balance change is expected.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>3.4</td>
    <td>Verify that it is not possible to withdraw tokens from the pool balance, during a flash loan. This can be implemented by using a flash loan amount parameter to check against the flash loan amount and the pool balance.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>4</strong></td>
    <td><strong>Liquidity Pools</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>4.1</td>
    <td>Confirm that the mechanisms for asset price calculation are safeguarded against attacks by price oracle manipulation. One remedy is to utilize a Time-Weighted Average Price (TWAP) oracle to lessen the associated risk. Make sure the time frame used, such as one day, is of an adequate duration.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
<tr>
<tr>
    <td>4.2</td>
    <td>Ensure that the calculations are performed with a sufficient number of decimal precision. For example, using a high degree of base precision, like 24 decimals for computation, can lower the risks related to rounding down errors.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>4.3</td>
    <td>Set criteria for assessing service provider trustworthiness. If using an external oracle, certify the service provider is trustworthy. <br /> There are several factors to be considered: <br /> 1) Reputation and Track Record: Check the reputation of the oracle provider. A provider with a solid track record of reliability and honesty is less likely to compromise the data. Look at their history in the industry, and consider seeking feedback from their current or former clients. <br /> 2) Transparency: Transparency of operations is key. Can the provider demonstrate how their data is sourced and how they handle discrepancies? Do they have auditable and transparent systems? <br /> 3) Decentralization: Decentralized oracle solutions are often more reliable than centralized ones, as they're not under the control of a single entity. They utilize consensus mechanisms and multiple data inputs to verify data authenticity. <br /> 4) Data Quality and Speed: The oracle should source and deliver data in a quick and efficient manner. Check for the freshness of data, refresh rate, and latency. Remember that outdated or slow delivery of data could negatively impact business operations. <br /> 5) Security Measures: Ask about the security measures that are in place to protect their systems against cyber attacks or data manipulation. The provider should demonstrate a robust security setup, which might include encrypting sensitive data and regularly conducting security audits. <br />  6) SLAs (Service Level Agreements): Ensure the provider has stringent commitments to uptime and reliability in their SLAs. Downtime can be damaging, especially for time-critical applications. <br /> 7) Insurance and Liabilities: Check if the oracle provider has sufficient insurance to cover losses in case of compromise or failure. This can be critical especially when huge sums are at stake. <br /> 8) Regulatory Compliance: Make sure the provider complies with all relevant laws and regulations in the jurisdictions where the company operates.
</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>4.4</td>
    <td>Ensure a pause mechanism to prevent service to continue working during abnormal conditions, such as a black swan event.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>4.5</td>
    <td>Ensure Liquidity Pools (LPs) with deflationary tokens use a secure mechanism to update their rate and it cannot be updated in the same transaction. <br /> 1) Understanding the Application: The first step is to understand how reflection tokens work. Look at the smart contract and be sure to understand how transactions are taxed and how those taxes are redistributed among holders. Understanding the mechanics of these tokens will make it easier to explain them to users and aid in troubleshooting. <br />  2) Tracking Holder Balances: Remember that each transaction alters holder balances, which can make it harder to track each holder's balance using traditional methods. Inbuilt procedures in the smart contract should exist for accurate reflections. <br /> 3) Complexity with Exchanges: Exchanges may have difficulty using reflection tokens because most use a cold/hot wallet system, which can be incompatible with how reflection tokens work. Ensure that the specific exchanges where the token is listed support the deflationary nature of the tokens. <br /> 4) Understanding Redistribution Rate: Be aware of the percentages that are being redistributed. Higher rates might initially seem attractive but could lead to a more rapid burn and instability in the token's value. <br /> 5) Impact on Value: Depending on how reflection is implemented, the "actual" value of a holder's tokens can be hard to determine because though the total tokens increase, the total value remains constant. There may also be a degree of volatility accompanying the reflected increase in token quantity which is important to understand and monitor. <br /> 6) Smart Contract Check: Always double-check the smart contract for any hidden vulnerability especially within the transfer method. Make sure there is nothing in the contract that can be exploited by bad actors, such as unexpected minting or burning of tokens.
</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
    <td>4.6</td>
    <td>Make sure the project has its liquidity secured for an extended period to avoid abrupt withdrawals. This approach helps maintain financial stability and signifies commitment, which can boost investor confidence.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
<!-- Governance -->
<tr>
    <td><strong>5</strong></td>
    <td><strong>Governance</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>5.1</td>
    <td>Certify whether the decentralized application governance smart contract includes a mechanism that prohibits users from creating a proposal and having it approved within the same transaction.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>5.2</td>
    <td>Confirm that the contract in question follows a thoroughly tested Governance standard. A comprehensive testing protocol ensures the contract complies with tried-and-true standards from established protocols like Aave. This is important for consistency, reliability, and reducing risk in contract execution.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>5.3</td>
    <td>Ensure secure management of the project via a DAO or a multisig contract.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>5.4</td>
    <td>Certify the counting of votes is done correctly and according to what has been stipulated in the protocol.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>5.5</td>
    <td>Make sure to implement delays and interruption mechanisms to cope with unforeseen circumstances. For example, when the token price undergoes substantial manipulation, the requirement to acquire a majority of tokens significantly diminishes. Therefore, these safety measures are necessary to mitigate risks and protect the interests of the stakeholders.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>5.6</td>
    <td>Prioritize the usage of a 2-step transfer mechanism for governance tokens to address flash loan attack risks.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
</tbody>
</table>
