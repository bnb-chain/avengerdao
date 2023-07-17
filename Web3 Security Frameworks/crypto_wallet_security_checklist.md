# BNB Chain - Web3 Security Framework

### Crypto Wallet Security Checklist

Classification: **Restricted**

**Stage: Enquiry stage (40)**

**Introduction**:

The Web3 Security Framework Initiative is a collaborative effort to promote the adoption of best practices in web3 security. The initiative aims to minimize the risks associated with security vulnerabilities and hacks, which have become increasingly prevalent in the web3 space. Moreover, projects that demonstrate full compliance with our rigorous guidelines will earn an on-chain certificate recognized by all the AvengerDAO members on the BNB Chain ecosystem.

This document serves as a comprehensive checklist of the critical elements surrounding the secure management of crypto wallets.

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
        <tr>
            <td><strong>1</strong></td>
            <td><strong>General</strong></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>1.1</td>
            <td>Define an evolutive policy outlining the organization's approach to securing cryptocurrency wallets that should be communicated to all employees and stakeholders and reviewed and updated regularly. Such a document will contain the measures taken in the elements below.</td>
            <td>High</td>
            <td><input type="checkbox"></td>
            <td></td>
        </tr>
        <tr>
            <td>1.1.1</td>
            <td>Define the different purposes of the project's wallets used by a project and the amount limit to reduce impact in case of a hack or leak. Eg: wallets for treasury, development and testing purposes, payment, etc.
            </td>
            <td>high</td>
            <td><input type="checkbox"></td>
            <td></td>
        </tr>
        <tr>
            <td>1.1.2</td>
            <td>Establish roles and responsibilities associated with managing wallet security topics as in a responsibility matrix.</td>
            <td>High</td>
            <td><input type="checkbox"></td>
            <td></td>
        </tr>
        <tr>
            <td><strong>2</strong></td>
            <td><strong>Education and Training</strong></td>
            <td></td>
            <td></td>
            <td></td>
        </tr>
        <tr>
            <td>2.1</td>
            <td>Provide team members with regular training around wallet security and best practices.</td>
            <td>High</td>
            <td><input type="checkbox"></td>
            <td></td>
        </tr>
        <tr>
            <td>2.2</td>
            <td>Maintain internal documentation of best practices to be followed by team members and new joiners.</td>
            <td>High</td>
            <td><input type="checkbox"></td>
            <td></td>
        </tr>
        <tr>
            <td>2.3</td>
            <td>Ensure team members are fully aware of new trends in phishing, ice phishing, and social engineering attacks.</td>
            <td>High</td>
            <td><input type="checkbox"></td>
            <td></td>
        </tr>
        <!-- Wallet Software and Hardware Selection -->
<tr>
    <td><strong>3</strong></td>
    <td><strong>Wallet Software and Hardware Selection</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>3.1</td>
    <td>Certify to use a wallet that uses secure/audited cryptographic libraries.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>3.2</td>
    <td>The wallet development team should ensure the secure integration of third-party solutions, this includes creating mechanisms to switch solutions without impacting the business.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>3.3</td>
    <td>Certify the wallet software is continually updated by the team to integrate any security patch.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>3.4</td>
    <td>Certify the wallet solution chosen has been thoroughly audited for security vulnerabilities and that they provide vulnerability remediation in a timely manner.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>3.5</td>
    <td>Hardware wallets should be purchased through formal channels to avoid supply chain attacks.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<!-- Operations -->
<tr>
    <td><strong>4</strong></td>
    <td><strong>Operations</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>4.1</td>
    <td>Document and track the list of wallets and their purposes. Avoid using wallets for purposes they were not intended to.</td>
    <td>TBD</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>5</strong></td>
    <td><strong>Wallet Sharing</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>5.1</td>
    <td>Define secure processes for sharing wallet sensitive information among developers.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>6</strong></td>
    <td><strong>Single point of failure</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>6.1</td>
    <td>To reduce the risk associated with stolen or leaked private keys, wallets with funds should use a security solution providing redundancy and access control - such as Smart Contract Wallets (Multi-signature), Multi-party Computation Wallets, and Multi-Factor Authentication (MFA) mechanisms. Note: Multisig wallets and MPC wallets are the preferred solution from a security perspective.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>6.2</td>
    <td>Multisig Wallet threshold should be at least 50% of the total number of owners.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>6.3</td>
    <td>Accounts associated with roles, having elevated privileges in smart contracts should also be assigned to several accounts using a redundant solution such as Smart Contract Wallet (Multi-Signature).</td>
    <td>Critical</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>6.4</td>
    <td>Make sure to implement mechanisms for the redundancy of wallets so that they are not lost in case of unexpected events.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<!-- Phishing attacks -->
<tr>
    <td><strong>7</strong></td>
    <td><strong>Phishing attacks</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>7.1</td>
    <td>Define guidelines for developers when working with wallets with funds - using a secure environment and tools, such as secure and up-to-date tools, browsers, and usage of only secure extensions to prevent known phishing attacks.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>7.2</td>
    <td>Ensure tools used for development are strictly used for that purpose and have no unstrusted 3rd party extensions.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>8</strong></td>
    <td><strong>Development Lifecycle</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>8.1</td>
    <td>Define a list of secure wallet software that can be used by team members and ensure they are used.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>8.2</td>
    <td>Define access control measures, following the principle of least privileges, for team members to use the private keys and access project funds.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>8.3</td>
    <td>Define guidelines for storing private keys encrypted in the local environment. Private keys shouldn’t be stored or shared in plain text.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>8.4</td>
    <td>To prevent indiscriminate usage and manipulation of wallets in an environment not controlled by the project, define the process and access control for users to use wallets in defined environment.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>9</strong></td>
    <td><strong>Wallets and Servers</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>9.1</td>
    <td>Use secure solutions to store private keys on test and production servers such as Hardware security modules and Key Management Systems.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>9.2</td>
    <td>Define secure guidelines for storing private keys associated with the production testing environment encrypted on test servers and ensure secure access control.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>9.3</td>
    <td>Certify the usage of at least one different wallet for testing environments and for production environments.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<!-- Treasury -->
<tr>
    <td><strong>10</strong></td>
    <td><strong>Treasury</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>10.1</td>
    <td>Implement monitoring and alerting mechanisms to detect moving funds.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>10.2</td>
    <td>Keep track of wallets used for which purposes.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>10.3</td>
    <td>Create a straightforward process for the management of such wallets, authorized users, process steps, and usage use cases.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>10.4</td>
    <td>Clearly define the standard for secure wallet solutions for treasury wallets for the project combining some of the following solutions: cold wallet solutions or hardware wallets, multisig, and MFA. And Implement it</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>10.5</td>
    <td>Create a straightforward procedure for when migrating funds to another wallet, with an internal chain of approval</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>10.6</td>
    <td>Create a process for when changing any software or hardware associated with the treasury wallets.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td><strong>11</strong></td>
    <td><strong>Incident Management</strong></td>
    <td></td>
    <td></td>
    <td></td>
</tr>
<tr>
    <td>11.1</td>
    <td>Create an incident response protocol to secure funds for the different scenarios where private keys are compromised - The process could be different for each type of wallet - Treasury wallets, wallets with elevated roles in smart contracts, etc.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
<tr>
    <td>11.2</td>
    <td>Rehearse the incident response protocol to ensure its effectiveness.</td>
    <td>High</td>
    <td><input type="checkbox"></td>
    <td></td>
</tr>
    </tbody>
</table>
