# BNB Chain - Web3 Security Framework

### Business Continuity Best Practices Checklist

Classification: **Restricted**

**Stage: Publication stage (60)**

**Introduction**:

The Web3 Security Framework Initiative is a collaborative effort to promote the adoption of best practices in web3 security. The initiative aims to minimize the risks associated with security vulnerabilities and hacks, which have become increasingly prevalent in the web3 space. Moreover, projects that demonstrate full compliance with our rigorous guidelines will earn an on-chain certificate recognized by all the AvengerDAO members on the BNB Chain ecosystem.

This document serves as a comprehensive checklist of the critical elements surrounding Business Continuity best practices.

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
    <!-- Project Funds -->
<tr>
    <td><strong>1</strong></td>
    <td><strong>Project Funds</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>1.1</td>
    <td>Ensure the project's fund allocation is designed to sustain through a bear market by implementing resilient financial strategies. Such strategies may include maintaining a reserve fund, substantial enough to support the business operations and associated expenses for at least a year, which is the typical duration of a bear market.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>1.2</td>
    <td>Safeguard project funds by employing cold storage or multi-signature wallets adhering to industry standards such as Ledger, Trezor, or <a href="https://multisig.bnbchain.org/welcome">BNBChain's Multi-Sig Wallet Service</a>. Enforce a threshold mandating over half of the owners' threshold for secure transactions. Develop transparency within the team concerning fund management, including judicious division of funds across wallets and precise record maintenance.</td>
    <td>Critical</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>1.3</td>
    <td>Outline protective measures that could be executed to safeguard the community in the event of a significant incident, like a hack. These measures should incorporate 1) prompt and effective communication with the community, 2) restitution plans informed by factors such as the cash amount lost in the hack, and the process of compensation for the impacted users. Additionally, 3) strategize plans to quickly reduce hack-induced damages, strategies that may entail a temporary halt of crucial operations.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>

<!-- Token Vesting -->
<tr>
    <td><strong>2</strong></td>
    <td><strong>Token Vesting</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>2.1</td>
    <td>Implement measures to discourage team members and investors from rapidly selling off their crypto assets, also known as 'dumping.' This could be achieved through the establishment of clear policies and guidelines promoting long-term holding.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>2.2</td>
    <td>Ensure to clearly communicate to stakeholders about the internal token vesting periods. Simultaneously, it's necessary to implement secure methods for token vesting. These can involve using trusted vesting services or setting up independent smart contract templates. An example of a reliable vesting code template is <a href="https://github.com/OpenZeppelin/openzeppelin-contracts/blob/master/contracts/finance/VestingWallet.sol">OpenZeppelin’s VestingWallet</a> template.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>

<!-- Systemic Risks -->
<tr>
    <td><strong>3</strong></td>
    <td><strong>Systemic Risks</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>3.1</td>
    <td>Prepare a well-defined remediation plan that reacts effectively to significant market price volatility. This plan should involve 1) Risk Assessment to identify and evaluate potential risks due to price fluctuations; 2) Preventative Measures, which are strategies aimed at reducing the potential negative impacts on business operations derived from market instability; and finally, 3) Response and Recovery procedures including operational responses and sound liquidity management to reinforce the continuous operation of the business.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
<tr>
<tr>
    <td>3.2</td>
    <td>Set up a system to identify and keep track of liquidity pools that utilize the project token and regularly evaluate their associated risks. This should involve noting the DEX liquidity pools' addresses, determining the current pool values, establishing an acceptable percentage for liquidity changes before intervention is needed, counting the existing LP tokens and examining the amount of locked liquidity, if applicable. A Risk Matrix system can be used to evaluate associated risks, considering multiple factors such as the duration LP tokens are locked, the sufficiency of liquidity for every pool, and connections between liquidity and other primary contracts. As a guiding principle, ensure the liquidity pools monitored do not carry high-risk status.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>3.3</td>
    <td>Develop precise operational guidelines that include a defined set of procedures, principles, and standards, designed to streamline business processes and drive consistency across the organization. These guidelines should also incorporate contingency plans to manage and mitigate risks in scenarios where operations deviate from the norm due to unforeseen circumstances. These contingency plans should outline a clear response framework detailing necessary actions and responsible personnel.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>3.4</td>
    <td>Put together actionable contingency plans for each potential risk. This involves analyzing all facets of the business to catalogue possible uncertainties and vulnerabilities. For each identified risk, establish guidelines and procedures to prevent, minimize, or effectively respond to its occurrence. This should include a clear chain of command, specific tasks assigned to individuals or teams, and, if needed, resource allocation for managing the situation.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
    
</tr>
<!-- Partnerships Relations -->
<tr>
    <td><strong>4</strong></td>
    <td><strong>Partnerships Relations</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>4.1</td>
    <td>For each partnership, pinpoint possible downstream contagion risks, where significant events within partner projects could initiate instability within the primary project. To reduce dependence risks inherent to partnerships, guarantee the partner project's security and assess the level of engagement with the partner undertaking. Essential to this process is the establishment of clear contingency plans and standard operating procedures through communication with downstream partners. It is vital to meticulously document these procedures and routinely review them to ensure their efficacy.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>

<!-- Entity Incident Response and Decentralization -->
<tr>
    <td><strong>5</strong></td>
    <td><strong>Entity Incident Response and Decentralization</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>5.1</td>
    <td>Create potential incident scenarios, pick suitable response tools, and outline detailed handling procedures. Simulate these scenarios in testing, and evaluate the response for improvement. Regularly repeat this process adapting to system changes and emerging threats.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
<tr>
<tr>
    <td>5.2</td>
    <td>Ensure roles and responsibilities in the decentralized organization are clearly defined and updated over time. In a decentralized organization, decision making can be influenced by not only the top level executives, but by senior, mid and lower level managers within the organization as well. Although traditional titles like CEO, CTO, and COO might persist, the power attached to each role should be dispersed more uniformly.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>5.3</td>
    <td>To avoid decision-making centralization, it's essential to delegate decision-making authority among various organization members. An effective approach to administer and execute decisions might involve the use of a Decentralized Autonomous Organization (DAO), empowered by a smart contract, responsible for updating the project's core contracts. A popular strategy entails utilizing tokenization, where members acquire voting rights proportional to their token holdings.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>5.4</td>
    <td>Establish clear governance rules and use suitable consensus mechanisms to balance power. Incentivize member participation and ensure transparency in all aspects. Implement strong risk management against internal and external threats. Educate everyone involved about their roles and compliance with relevant laws, adapting a model that best suits the organization.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
    </tbody>
</table>
