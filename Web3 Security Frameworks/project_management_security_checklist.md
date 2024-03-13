# BNB Chain - Web3 Security Framework

### Project Management Best Practices Checklist

Classification: **Restricted**

**Stage: Publication stage (60)**

**Introduction**:

The Web3 Security Framework Initiative is a collaborative effort to promote the adoption of best practices in web3 security. The initiative aims to minimize the risks associated with security vulnerabilities and hacks, which have become increasingly prevalent in the web3 space. Moreover, projects that demonstrate full compliance with our rigorous guidelines will earn an on-chain certificate recognized by all the AvengerDAO members on the BNB Chain ecosystem.

This document serves as a comprehensive checklist of the critical elements surrounding the web3 project management best practices.

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
    <!-- Usage of technologies -->
<tr>
    <td><strong>1</strong></td>
    <td><strong>Technology Selection</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>1.1</td>
    <td>Certify the list of solutions the decentralized application is allowed to integrate and keep track of any vulnerability that might be detected.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>1.2</td>
    <td>Ensure the separation of roles in Web applications. The backend handles processing, external communication, key management, and integration, while the frontend displays data and manages user interactions. This separation improves efficiency, debugging, security, scalability, and supports multiple platforms, boosting development, protection, and adaptability.</td>
    <td>Medium</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>1.3</td>
    <td>Certification of a remediation plan for issues with Infrastructure, oracles, bridges, tech providers, etc.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>2</strong></td>
    <td><strong>Development Lifecycle</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><strong>2.1</strong></td>
    <td><strong>Design</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>2.1.1</td>
    <td>Formally define the business case and the technical solution to address the problem to be solved.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>2.2</strong></td>
    <td><strong>Development</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>2.2.1</td>
    <td>Ensure there are processes in place to track vulnerabilities in external dependencies.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>2.3</strong></td>
    <td><strong>Testing and Validation</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>2.3.1</td>
    <td>Several testing strategies should be in place (unit testing, integration testing, regression testing as well as stress testing) in addition to web3 specific security testing including static and dynamic code analysis, fuzzing testing and formal verification on all business-critical scenarios. Such scenarios should be clearly documented and results should be validated in the project development lifecycle before the production release.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>2.3.2</td>
    <td>Stress testing scenarios [non-exhaustive]: Adverse market conditions, Adverse token price fluctuations, Issues with key inputs (eg. oracle pricing going offline, etc.), Edge-case/extreme event situations etc. Assess the impact on the project, other projects, and the overall ecosystem of these stress-testing scenarios.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>2.4</strong></td>
    <td><strong>Continuous Integration</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>2.4.1</td>
    <td>Ensure continuous integration pipelines are in place and perform the unit, integration tests.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>2.4.2</td>
    <td>Make certain that the continuous integration process incorporates rigorous security tests. Include techniques such as Static and Dynamic Application Security Testing (SAST & DAST), Interactive Application Security Testing (IAST), and regular Security Scanning. Utilize a selection of these methods to ensure maximum efficiency and efficacy of the security inspections.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>2.5</strong></td>
    <td><strong>Deployment</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>2.5.1</td>
    <td>Certify the correctness of the deployment scripts and that they include automatic publication (verification) of the smart contract code on the blockchain explorer.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>2.5.2</td>
    <td>Make certain to validate the source code for smart contracts on the appropriate blockchain explorers for the specific chain where projects are deployed. For example, when deploying on BSC, follow the guide for contract verification programmatically provided in this <a href="https://docs.bscscan.com/tutorials/verifying-contracts-programmatically">link</a>.</td>
    <td>Medium</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>2.6</strong></td>
    <td><strong>Monitoring</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>2.6.1</td>
    <td>Ensure the capacity of the project to monitor on-chain the project smart contract activity once the deployment is complete.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>2.6.2</td>
    <td>In case of an unexpected event such as funds being siphoned, an alert system should be triggered and the project's point of contact should be notified.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>

<!-- Decentralized Application -->
<tr>
    <td><strong>3</strong></td>
    <td><strong>Decentralized Application</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><strong>3.1</strong></td>
    <td><strong>Web2 Stack</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><strong>3.1.1</strong></td>
    <td><strong>Infrastructure</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>3.1.1.1</td>
    <td>Ensure operations guidelines for infrastructure management and incident response are in place. This could include examples such as emergency failover procedures, disaster recovery strategies, and incident triage process documentation. Reference or link to appropriate documentation and scenario-based solutions for managing common or high-impact issues.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>3.1.1.2</td>
    <td>Ensure the implementation of secure infrastructure security best practices.This includes practices such as adhering to the Principle of Least Privilege (PoLP), which limits user and system privileges to only what is necessary. Regularly patching and updating systems help safeguard against known vulnerabilities. Additional protective measures include implementing firewalls and Intrusion Detection/Prevention Systems to track and block suspicious network activity. Data encryption at rest and in transit is also essential to prevent unauthorized access. Furthermore, initiating multi-factor authentication (MFA) adds an extra layer of security access to systems.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>3.1.2</strong></td>
    <td><strong>Network</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>3.1.2.1</td>
    <td>Ensure sufficient network security, using firewalls and DDoS attack prevention mechanisms.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>3.1.3</strong></td>
    <td><strong>Software Security</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>3.1.3.1</td>
    <td>Ensure the security of frontend and backend applications using testing, and static and dynamic code analysis, and are free of any OWASP vulnerabilities.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>3.1.3.2</td>
    <td>Ensure RPC and API endpoints are properly configured and secured, via access control, authorization, and authentication.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>3.1.4</strong></td>
    <td><strong>Cryptographic Keys Secure Storage</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>3.1.4.1</td>
    <td>Use secure means for storing cryptographic keys and seed phrases such as Hardware Security Modules and Key Management Services.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>3.1.5</strong></td>
    <td><strong>Secured Equipment</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>3.1.5.1</td>
    <td>Establish a policy to guarantee that all personnel utilizes secure devices equipped with essential firewall and antivirus security measures.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>3.2</strong></td>
    <td><strong>CVEs and Tech Stack</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>3.2.1</td>
    <td>Implement a procedure for regularly monitoring and addressing new Common Vulnerabilities and Exposures (CVEs) across the entire technology stack.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>3.3</strong></td>
    <td><strong>General Security</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>3.3.1</td>
    <td>Establish mechanisms to ensure the protection and maintenance of service availability, confidentiality, and integrity through certifiable means.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>3.4</strong></td>
    <td><strong>Risk Management</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>3.4.1</td>
    <td>Put in place a strategy to adhere to established industry standards, such as ISO 27001, NIST Cybersecurity Framework, etc.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>3.5</strong></td>
    <td><strong>Transaction signing</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>3.5.1</td>
    <td>To reduce surface attacks on private keys and prevent their leakage, ensure that all project-related transactions and transactions generated for customer custodian wallet are signed offline.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<!-- Web3 Stack -->
<tr>
    <td><strong>4</strong></td>
    <td><strong>Web3 Stack</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><strong>4.1</strong></td>
    <td><strong>Wallet interface</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>4.1.1</td>
    <td>Ensure transactions appear clearly in the user's wallet prior to signing, ensuring readability and transparency, and preventing the signing of undesired transactions. Make certain the details of transactions, such as From address, To address, and Funds balance change, are clearly decipherable. Use wallet applications or 3rd party extensions that can render the transaction information in an understandable format.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>5</strong></td>
    <td><strong>Training</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>5.1</td>
    <td>Implement a comprehensive training program to ensure that all personnel are regularly updated on the latest security concepts and best practices. The training program should identify the training needs and set clear learning goals. Develop actionable training content tailored specifically to staff roles and levels of experience. Choose an appropriate delivery method, such as online modules or in-person workshops, for the training content. Finally, implement the program and organize its logistics, ensuring easy access and a suitable schedule for all personnel. Evaluate outcomes regularly and adjust the program as needed to ensure continual learning and improvement.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>6</strong></td>
    <td><strong>Audit</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>6.1</td>
    <td>To enhance the project security maturity, it is recommended to conduct periodic security audits with reputable security firms. As a guideline, carry out security audits quarterly, enlisting specialized firms like Trail of Bits, ConsenSys Diligence, or OpenZeppelin. The audit report should include an executive summary, the audit's scope, methodology deployed, a detailed report of findings ranked by their severity, as well as the conclusion. These reports help track the project’s security standing and ensure a constant framework for necessary enhancements.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>6.2</td>
    <td>Certify that all audit recommendations are implemented. To implement audit recommendations, start by reviewing and prioritizing them based on severity and impact on the platform's security. Assign measures to teams with clear understanding and timelines. Regularly monitor progress and troubleshoot roadblocks. Following implementation, reassess the platform's security to ensure all vulnerabilities are effectively addressed, thus maintaining consistent high security standards.</td>
    <td>Critical</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>7</strong></td>
    <td><strong>Tokens</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>7.1</td>
    <td>Implement a mechanism for continuously monitoring the project liquidity, including the health of DEX liquidity pools and the security of the platforms where the token is traded, to ensure the viability and stability of the token economy.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>8</strong></td>
    <td><strong>External Parties</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>8.1</td>
    <td>The list of dependencies of external projects should be clearly documented and updated over time. Eg: wrapped assets, vaults/farms, multi-protocol dependencies, libs (Openzeppelin) oracles (BNB, Chainlink), Dex for liquidity. This documentation needs to include the dependency's name, version, role, relevant links, and contact points. Regular updates to this document should be made every time there is an addition, removal or change in a dependency. Periodically reviewing this document for accuracy and any necessary updates or vulnerability checks is also crucial to maintain a clear and updated overview of the project's dependencies at all times.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>8.2</td>
    <td>Verify there are channels of communication existing with external parties and partners. Start by identifying who these entities are. Define the specific communication mediums used with each and ensure there are assigned points of contact for continuous management. Create a proactive and agreed-upon communication strategy for timely sharing of essential information. Regularly test these channels for their effectiveness, and adjust as necessary to maintain productive communication and collaborative relationships.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>8.3</td>
    <td>Projects should not only rely on notification and communication because of delays, it becomes fundamental they also monitor on-chain dependencies. Partners should be able to provide means to do so.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<!-- Change Management -->
<tr>
    <td><strong>9</strong></td>
    <td><strong>Change Management</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>9.1</td>
    <td>Set firm guidelines for roles and responsibilities pertaining to the governance, management, and security of smart contracts, funds, and internal systems. This will aid in accountability and informed decision-making. Hold each person accountable for their roles to boost effective decision-making. Use monitoring utilities for performance tracking and activity logs, facilitating effectiveness evaluations. Tools can encompass security trackers, system monitors, and performance management systems. Such a strategy boosts operation optimization and effective decision-making by accurately defining, assigning, and overseeing each role.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>9.2</td>
    <td>Verify the existence of a process to make changes in a timely manner, with the chain of internal validation.</td>
    <td>Medium</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>9.3</td>
    <td>Additionally, establish a tested and reliable process for safely resolving production issues, enabling prompt corrective action to be taken with confidence, and following an internal chain of validation to ensure prompt and effective resolution.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>10</strong></td>
    <td><strong>Incident Response</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td><strong>10.1</strong></td>
    <td><strong>Incident Response for External Causes</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>10.1.1</td>
    <td>Verify that channels work both ways and that your project is aware of the means of communication of your external partner in case they suffer from an incident.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>10.1.2</td>
    <td>Certify that remediation protocols are in place in case external partners suffer severe business impact. eg: hack.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>10.2</strong></td>
    <td><strong>Incident Response for Internal Causes</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>10.2.1</td>
    <td>Ensure that partners with critical dependencies are aware of your security processes and if they have to participate in the project's incident response activity.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>10.2.2</td>
    <td>Certify that internal teams and external dependencies have rehearsed incident response protocols, where they perform their expected role.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>10.2.3</td>
    <td>It is recommended for projects to put in place means for responding automatically to monitoring alerts of potential hacks to try to prevent an attack, without impacting the business..</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>10.3</strong></td>
    <td><strong>Communication</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>10.3.1</td>
    <td>Ensure the existence of dedicated channels to communicate with the community and partners about unexpected events in a timely manner.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>11</strong></td>
    <td><strong>Post Incident</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>11.1</td>
    <td>Certify the existence of a process for the establishment of a post-mortem following major unexpected events such as hacks, service unavailability, etc. <br /> The template commonly includes the following sections: <br /> 1) Event Overview: This includes details of when the incident occurred, the duration of the issue, and a brief summary of the event. <br /> 2) Impact Analysis: This section explains the overall impact of the event on the services, systems, or customers. <br /> 3) Timeline of Events: This is a detailed account of the incident from the moment it happened until it was resolved. It's important to document all the steps that were taken during this period. <br /> 4) Findings: This section can include logs, reports, or other data that shed light on the root cause of the incident. <br /> 5) Root Cause Analysis: This is a detailed analysis of why the event took place and the deficiencies that led to it. <br /> 6) Corrective Actions Taken: Here, list the immediate steps taken to mitigate the effects of the incident. <br /> 7) Preventive Measures and Recommendations: This is a crucial section that identifies actions that should be taken to prevent similar occurrences in the future.
</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
</tbody>
</tables>
