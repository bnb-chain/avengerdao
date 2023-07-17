# BNB Chain - Web3 Security Framework

### Decentralized Finance Practices Checklist

Classification: **Restricted**

**Stage: Enquiry stage (40)**

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
    <td>Verify that the decentralized application (Dapp) does not assume users can only send tokens using its smart contract functions. Tokens can be sent using the token smart contract transfer function or a self-destruct mechanism.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>1.2</td>
    <td>Certify the separation of the deposit logic from the reward calculation as reserves might impact the calculation.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>1.3</td>
    <td>Certify there are mechanisms to pause the contracts in case of the detection of a compromised or malfunctioning dependencies such as oracles.</td>
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
    <td>When using an on-chain price calculation mechanism, certifying the price of an asset cannot be manipulated in the same transaction, manipulating the source data, via flash loans for instance.</td>
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
    <td>Verify the centralized actor cannot be incentivized to push altered data to the data source.</td>
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
    <td>Prevent reentrancy attacks in your flash loan function.</td>
    <td>Critical</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>3.3</td>
    <td>Certify the mechanism calculating the number of tokens before and after the loans is not vulnerable.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>3.4</td>
    <td>Verify that it is not possible to withdraw tokens from the pool balance, during a flash loan.</td>
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
    <td>Ensure that the asset price calculation mechanisms cannot be attacked by price oracle manipulation.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
<tr>
<tr>
    <td>4.2</td>
    <td>Verify calculations are done with enough precision decimals.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>4.3</td>
    <td>If using an external oracle, certify the service provider is trustworthy.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>4.4</td>
    <td>Ensure a pause mechanism to prevent service to continue working in abnormal conditions.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>4.5</td>
    <td>Avoid using reflection tokens in liquidity/lending pools. If necessary, ensure a secure mechanism to update their rate or that the reflection token smart contract doesn't enable means to manage its supply.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
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
    <td>Please confirm whether the decentralized application governance smart contract includes a mechanism that prohibits users from creating a proposal and having it approved within the same transaction.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>5.2</td>
    <td>Ensure the contract is a Governance standard that has been fully tested.</td>
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
    <td>Ensure the usage of delays and interruption mechanisms exist in case of unexpected situations.</td>
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
