# BNB Chain - Web3 Security Framework

### Project Management Best Practices Checklist

Classification: **Restricted**

**Stage: Enquiry stage (40)**

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
    <td>TBD</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>1.2</td>
    <td>Ensure the separation of roles of your Web application, most processing, external communication, management of keys, and solution integration should be done in the backend application, leaving the frontend for displaying backend data and managing user interaction and inputs.</td>
    <td>TBD</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>1.3</td>
    <td>Certification of a remediation plan for issues with Infrastructure, oracles, bridges, tech providers, etc.</td>
    <td>TBD</td>
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
    <td>TBD</td>
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
    <td>TBD</td>
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
    <td>Several testing strategies should be in place (unit testing, integration testing, regression testing as well as stress testing), at least for the business-critical scenarios. Such scenarios should be clearly documented and results should be validated in the project development lifecycle before the production release.</td>
    <td>TBD</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>2.3.2</td>
    <td>Stress testing scenarios [non-exhaustive]: Adverse market conditions, Adverse token price fluctuations, Issues with key inputs (eg. oracle pricing going offline, etc.), Edge-case/extreme event situations etc. Assess the impact on the project, other projects, and the overall ecosystem of these stress-testing scenarios.</td>
    <td>TBD</td>
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
    <td>Ensure continuous integration pipelines are in place and perform the unit and integration tests.</td>
    <td>TBD</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>2.4.2</td>
    <td>Ensure security tests are also part of the continuous integration process.</td>
    <td>TBD</td>
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
    <td>Certify the correctness of the deployment scripts.</td>
    <td>TBD</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>2.5.2</td>
    <td>Verify smart contracts on blockchain explorers for the specific chain the projects are being deployed.</td>
    <td>TBD</td>
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
    <td>TBD</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>2.6.2</td>
    <td>In case of an unexpected event such as funds being siphoned, an alert system should be triggered and the project point of contact should be notified.</td>
    <td>TBD</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
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
    <td>Ensure operations guidelines are in place for infrastructure management and incident response.</td>
    <td>TBD</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>3.1.1.2</td>
    <td>Ensure the implementation of secure infrastructure security best practices.</td>
    <td>TBD</td>
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
    <td>Ensure network security thanks to firewalls and DDoS attack prevention mechanisms.</td>
    <td>TBD</td>
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
    <td>TBD</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>3.1.3.2</td>
    <td>Ensure RPC and API endpoints are properly configured and secured, via access control, authorization, and authentication.</td>
    <td>TBD</td>
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
    <td>TBD</td>
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
    <td>TBD</td>
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
    <td>TBD</td>
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
    <td>TBD</td>
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
    <td>TBD</td>
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
    <td>TBD</td>
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
    <td>Ensure transactions appear clearly in the user's wallet prior to signing, ensuring readability and transparency, and preventing the signing of undesired transactions.</td>
    <td>TBD</td>
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
    <td>Implement a comprehensive training program to ensure that all personnel is regularly updated on the latest security concepts and best practices.</td>
    <td>TBD</td>
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
    <td>To enhance the project security maturity, it is recommended to conduct periodic security audits with reputable security firms.</td>
    <td>TBD</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>6.2</td>
    <td>Certify that all audit recommendations are implemented.</td>
    <td>TBD</td>
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
    <td>Implement a mechanism for continuously monitoring the projected liquidity, including the health of DEX liquidity pools and the security of the platforms where the token is traded, to ensure the viability and stability of the token economy.</td>
    <td>TBD</td>
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
    <td>The list of dependencies of external projects should be clearly documented and updated over time. Eg: wrapped assets, vaults/farms, multi-protocol dependencies, libs (Openzeppelin) oracles (BNB, Chainlink), Dex for liquidity.</td>
    <td>TBD</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>8.2</td>
    <td>Verify there are channels of communication existing with external parties and partners.</td>
    <td>TBD</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>8.3</td>
    <td>Projects should not only rely on notification and communication because of delays, it becomes fundamental they also monitor on-chain dependencies. Partners should be able to provide means to do so.</td>
    <td>TBD</td>
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
    <td>Establish clear definitions for roles and responsibilities regarding the governance, management, and security of smart contracts, funds, and internal systems to ensure accountability and effective decision-making.</td>
    <td>TBD</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>9.2</td>
    <td>It is common to find unexpected behaviors in a piece of software, and verify the existence of a process to make changes in a timely manner, with the chain of internal validation.</td>
    <td>TBD</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>9.3</td>
    <td>Additionally, establish a tested and reliable process for safely resolving production issues, enabling prompt corrective action to be taken with confidence, and following an internal chain of validation to ensure prompt and effective resolution.</td>
    <td>TBD</td>
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
    <td>TBD</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>10.1.2</td>
    <td>Certify that remediation protocols are in place in case external partners suffer severe business impact. eg: hack.</td>
    <td>TBD</td>
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
    <td>TBD</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>10.2.2</td>
    <td>Certify that internal teams and external dependencies have rehearsed incident response protocols, where they perform their expected role.</td>
    <td>TBD</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>10.2.3</td>
    <td>It recommends projects that have the means to stop an attack and fix the issue without impacting the business.</td>
    <td>TBD</td>
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
    <td>TBD</td>
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
    <td>Certify the existence of a process for the establishment of a post-mortem following major unexpected events such as hacks, service unavailability, etc.</td>
    <td>TBD</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
</tbody>
</tables>
