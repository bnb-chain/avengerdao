# BNB Chain - Web3 Security Framework

### Smart Contract Security Checklist

Classification: **Restricted**

**Stage: Enquiry stage (40)**

**Introduction**:

The Web3 Security Framework Initiative is a collaborative effort to promote the adoption of best practices in web3 security. The initiative aims to minimize the risks associated with security vulnerabilities and hacks, which have become increasingly prevalent in the web3 space. Moreover, projects that demonstrate full compliance with our rigorous guidelines will earn an on-chain certificate recognized by all the AvengerDAO members on the BNB Chain ecosystem.

This document serves as a comprehensive checklist of the critical elements surrounding the secure development of solidity smart contracts.

<table>
  <tr>
   <td><strong>Item id</strong>
   </td>
   <td colspan="2" ><strong>Security Check</strong>
   </td>
   <td><strong>Criticality</strong>
   </td>
   <td><strong>Is Project Compliant?</strong>
   </td>
   <td><strong>Comments</strong>
   </td>
  </tr>
  <tr>
   <td>
    <strong>1</strong>
   </td>
   <td colspan="5" >
    <strong><em>Audit</em></strong>
   </td>
  </tr>
  <tr>
   <td>
    1.1
   </td>
   <td colspan="2" >To reduce risks of vulnerabilities, audits are required for each major release. The audits should be performed by multiple auditing firms.
   </td>
   <td>High
   </td>
   <td>
   <ol>
<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    1.2
   </td>
   <td colspan="2" >Audits scope should be comprehensive and include business logic correctness, proxy setup, access control, vulnerability findings, etc. 
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    1.3
   </td>
   <td colspan="2" >Following the audits, ensure all issues have been fixed and recommendations have been implemented.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    1.4
   </td>
   <td colspan="2" >Ensure your project is part of a bug bounty program
   </td>
   <td>Medium
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>2</strong>
   </td>
   <td colspan="5" >
    <strong><em>Test Coverage</em></strong>
   </td>
  </tr>
  <tr>
   <td>
    2.1
   </td>
   <td colspan="2" >All non-trivial functions should be tested.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    2.2
   </td>
   <td colspan="2" >Business-critical functions should be thoroughly tested against all edge cases. 
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    2.3
   </td>
   <td colspan="2" >Certify the exactitude of the expected behavior of functions and business flows.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    2.3
   </td>
   <td colspan="2" >Certify that all scenarios raising exceptions are also tested and that exception management works as expected (eg: matching internal exceptions with customer-facing error code/message) 
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    2.4
   </td>
   <td colspan="2" >Verify the code specifications using formal verification.
   </td>
   <td>Medium
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>3</strong>
   </td>
   <td colspan="5" >
    <strong><em>Solidity Specifics</em></strong>
   </td>
  </tr>
  <tr>
   <td>
    <strong>3.1</strong>
   </td>
   <td colspan="5" >
    <strong>General</strong>
   </td>
  </tr>
  <tr>
   <td>
    3.1.1
   </td>
   <td colspan="2" >Ensure development teams use security scanning tools.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.1.2
   </td>
   <td colspan="2" >Use BSCSCan to verify all deployed contracts and their implementation
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.1.3
   </td>
   <td colspan="2" >Verify smart contracts are not using send() or transfer() functions to send infrastructure tokens.
   </td>
   <td>Medium
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>3.2</strong>
   </td>
   <td colspan="5" >
    <strong>Immutability</strong>
   </td>
  </tr>
  <tr>
   <td>
    3.2.1
   </td>
   <td colspan="2" >
    Ensure smart contracts do not rely on the immutability of another smart contract, if the latter has a self-destruct or delegate-call mechanism.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>3.2</strong>
   </td>
   <td colspan="5" >
    <strong>Data</strong>
   </td>
  </tr>
  <tr>
   <td>
    3.2.1
   </td>
   <td colspan="2" >Blockchain ledgers are publicly accessible by design. Therefore it is recommended that smart contract data should be classified according to its level of confidentiality.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.2.2
   </td>
   <td colspan="2" >Verify the confidentiality framework applied to the decentralized application data complies with regulations around the world. eg: GDPR, PCI-DSS, etc.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.2.3
   </td>
   <td colspan="2" >Ensure smart contracts' critical business logic does not rely solely on data that can be predictable or manipulated by validators, such as block timestamp, block number, block hash…
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>3.3</strong>
   </td>
   <td colspan="5" >
    <strong>Complex Data Structure</strong>
   </td>
  </tr>
  <tr>
   <td>
    3.3.1
   </td>
   <td colspan="2" >Ensure the size of data stays stable over time so that gas 
<p>
consumption remains stable.
   </td>
   <td>Medium
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.3.2
   </td>
   <td colspan="2" >Ensure proper validation of data to prevent runtime exceptions such as stack overflow, out of gas, and stack too deep.
   </td>
   <td>Medium
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>3.4</strong>
   </td>
   <td colspan="5" >
    <strong>Dependencies</strong>
   </td>
  </tr>
  <tr>
   <td>
    3.4.1
   </td>
   <td colspan="2" >Certify all decentralized applications' external dependencies are trusted sources.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.4.2
   </td>
   <td colspan="2" >Ensure such dependencies have been properly tested before integrating them.
   </td>
   <td>Medium
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.4.3
   </td>
   <td colspan="2" >Smart contract dependencies such as Libraries should be clearly identified and documented.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>`
   </td>
  </tr>
  <tr>
   <td>
    3.4.4
   </td>
   <td colspan="2" >Ensure dependency versions are clearly specified.
   </td>
   <td>Low
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>3.5</strong>
   </td>
   <td colspan="5" >
    <strong>Business Logic</strong>
   </td>
  </tr>
  <tr>
   <td>
    3.5.1
   </td>
   <td colspan="2" >Ensure that whenever feasible, standard contracts are employed.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.5.2
   </td>
   <td colspan="2" >Certify that all crucial business flows are documented and comprehensively tested to avoid bugs and corner case exceptions.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.5.3
   </td>
   <td colspan="2" >Given the existence of front-running possibilities, and the risk of flash loan attacks, use adequate means to secure them.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.5.4
   </td>
   <td colspan="2" >Ensure the smart contract state is updated correctly when performing actions such as transfer, deposit, withdraw, etc…
   </td>
   <td>High
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.5.5
   </td>
   <td colspan="2" >Ensure that timelocks are used in relevant business flows where it makes sense. So that the projects have time to better observe and monitor decentralized applications app behavior and changes. It should be analyzed on a case-by-case basis.  
   </td>
   <td>Medium
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>3.6</strong>
   </td>
   <td colspan="5" >
    <strong>Arithmetics</strong>
   </td>
  </tr>
  <tr>
   <td>
    3.6.1
   </td>
   <td colspan="2" >Certify that your arithmetic operations are protected against unwanted underflow or overflow. 
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.6.2
   </td>
   <td colspan="2" >Verify the inequalities are used when comparing smart contract balance.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.6.3
   </td>
   <td colspan="2" >Verify the order of magnitude of calculations is correct.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.6.4
   </td>
   <td colspan="2" >Ensure the order of operations so that results do not lose precision. 
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.6.5
   </td>
   <td colspan="2" >Ensure divisions with integers are done safely.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>3.7</strong>
   </td>
   <td colspan="5" >
    <strong>Input validation</strong>
   </td>
  </tr>
  <tr>
   <td>
    3.7.1
   </td>
   <td colspan="2" >
    Ensure user-defined inputs are sanitized and checked as soon as possible in the smart contract function code.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.7.2
   </td>
   <td colspan="2" >
    For input validation, ensure the usage of require or revert.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.7.3
   </td>
   <td colspan="2" >
    To prevent privilege escalation and replay attacks, functions utilizing off-chain signed cryptographic signatures for authorization must ensure that the signature is not susceptible to reuse.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.7.4
   </td>
   <td colspan="2" >
    Assertions with the assert keyword should be used to evaluate invariants' states.
   </td>
   <td>Medium
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>3.8</strong>
   </td>
   <td colspan="5" >
    <strong>Reentrancy</strong>
   </td>
  </tr>
  <tr>
   <td>
    3.8.1
   </td>
   <td colspan="2" >
    Ensure that the smart contract state is updated before giving the control execution flow to the external unknown smart contract. 
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.8.2
   </td>
   <td colspan="2" >
    Ensure secure mechanisms are in place to prevent same-function and cross-function reentrancy, such as checks, effects, and interactions principles or Reentrancy solutions.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.8.3
   </td>
   <td colspan="2" >
    Special attention should be paid when using to the use of the transfer function of ERC721 and ERC1155 tokens to ensure that the data is updated before the transfer operation
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.8.4
   </td>
   <td colspan="2" >
    Ensure the transferring assets that delegate the execution flow to other smart contracts is done securely. eg: The ERC721 standard code, which triggers the invocation of the onERC721Received function
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.8.5
   </td>
   <td colspan="2" >
    Certify functions with protection against Reentrancy attacks are tested for such scenarios.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>3.9</strong>
   </td>
   <td colspan="5" >
    <strong>Exceptions</strong>
   </td>
  </tr>
  <tr>
   <td>
    3.9.1
   </td>
   <td colspan="2" >
    Always verify internal and external call return values for unexpected events and define behavior accordingly.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.9.2
   </td>
   <td colspan="2" >
    Ensure custom exceptions are created to enhance the exception handling capabilities and code readability.
   </td>
   <td>Medium
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>3.</strong>10
   </td>
   <td colspan="5" >
    <strong>Gas Consumption</strong>
   </td>
  </tr>
  <tr>
   <td>
    3.10.1
   </td>
   <td colspan="2" >
    Verify that the Dapp smart contract functions are implemented in a manner that gas consumption persists stable over time. 
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.10.2
   </td>
   <td colspan="2" >
    Always provide enough gas when performing a sub-call to another smart contract. The gas calculation should be justified as it may vary over time.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>3.11</strong>
   </td>
   <td colspan="5" >
    <strong>Denial of Service</strong>
   </td>
  </tr>
  <tr>
   <td>
    3.11.1
   </td>
   <td colspan="2" >
    Ensures proper exception management when transferring crypto assets, such as using try-and-catch blocks.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.11.2
   </td>
   <td colspan="2" >
    Avoid using unbounded loops or looping over user-defined parameters without proper controls. If so, ensure the logic execution scale over time with the use of the smart contract. 
   </td>
   <td>Medium
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.11.3
   </td>
   <td colspan="2" >
    Self-destruct usage should be avoided as assets other than infrastructure tokens and funds sent to the contract  \
after self-destruction would be lost. Also, smart contract data is not erased from the Blockchain history. Finally, self-destruction is irreversible. If really necessary, its usage should be documented and tested
   </td>
   <td>Low
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>3.12</strong>
   </td>
   <td colspan="5" >
    <strong>Monitoring and Alerting</strong>
   </td>
  </tr>
  <tr>
   <td>
    3.12.1
   </td>
   <td colspan="2" >
    Similar to web applications, smart contracts should be monitored as part of the operations of a running decentralized application. 
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.12.2
   </td>
   <td colspan="2" >
    The alerting system should also be implemented to detect and alert teams of unexpected behavior. 
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>3.13</strong>
   </td>
   <td colspan="5" >
    <strong>Low-Level Calls</strong>
   </td>
  </tr>
  <tr>
   <td>
    3.13.1
   </td>
   <td colspan="2" >
    Ensure proper management of errors in low-level calls as they do not raise exceptions.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.13.2
   </td>
   <td colspan="2" >
    Smart contracts should properly validate the response of a low-level call response, as it can be manipulated by the called smart contracts.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.13.3
   </td>
   <td colspan="2" >
    Avoid using delegatecall low-level calls, only use them if really necessary and only if the target contract is trusted and secure.
   </td>
   <td>Medium
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>3.14</strong>
   </td>
   <td colspan="5" >
    <strong>Upgradeable Contracts</strong>
   </td>
  </tr>
  <tr>
   <td>
    3.14.1
   </td>
   <td colspan="2" >
    Ensure the proxy upgradeability has access control and is only actionable with a wallet using a multiple-account solution.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.14.2
   </td>
   <td colspan="2" >
    Verify that the proxy and implementation deployment or upgrade process is done in one transaction so that they cannot be front-run.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.14.3
   </td>
   <td colspan="2" >
    For initialized implementations, verify that the proxy  implementation is initialized.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.14.4
   </td>
   <td colspan="2" >
    Certifying the proxy implementation cannot be destroyed. In such a scenario, the proxy contract would not be able to upgrade.
   </td>
   <td>High
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    3.14.5
   </td>
   <td colspan="2" >
    Ensure the upgradeable contract has no overlap between the storage used by the implementation contract and the one used by the proxy.
   </td>
   <td>Medium
   </td>
   <td>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>3.15</strong>
   </td>
   <td colspan="5" >
    <strong>Randomness</strong>
   </td>
  </tr>
  <tr>
   <td>
    3.15.1
   </td>
   <td colspan="2" >Certify that random numbers are generated in a secure fashion.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>4</strong>
   </td>
   <td colspan="5" >
    <strong><em>Architecture</em></strong>
   </td>
  </tr>
  <tr>
   <td>
    4.1
   </td>
   <td colspan="2" >
    Smart contracts are fundamentally immutable. Ensure that adequate patterns are used to enable smart contract code upgrading over time and in case of incidents.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    4.2
   </td>
   <td colspan="2" >
    Ensure that any ERC standard is implemented correctly, and validated thanks to a wide range of tests.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    4.3
   </td>
   <td colspan="2" >
    For visibility and state tracking, use events to announce state changes or business actions.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    4.4
   </td>
   <td colspan="2" >
    Ensure that at least the critical business flows have their external and internal dependencies clearly documented. Eg: oracles, liquidity pools, and smart contract standards.
   </td>
   <td>Medium
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    4.5
   </td>
   <td colspan="2" >
    If smart contract addresses require being deterministic, use the appropriate low-level call. Low-level calls aren’t recommended and should be used at your own risk. 
   </td>
   <td>Low
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>5</strong>
   </td>
   <td colspan="5" >
    <strong><em>Access Control</em></strong>
   </td>
  </tr>
  <tr>
   <td>
    5.1
   </td>
   <td colspan="2" >
    Verify smart contracts' functions' access follow the least privilege principle.  
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    5.2
   </td>
   <td colspan="2" >
    Ensure that users only have access to smart contracts they are intended to. 
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    5.3
   </td>
   <td colspan="2" >
    Certification of the access control on the web application side is aligned with the one existing in the smart contract.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    5.6
   </td>
   <td colspan="2" >
    The access control mechanism of a large decentralized application should be centralized for better control. 
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    5.7
   </td>
   <td colspan="2" >
    Verify the existence of reentrancy protection for functions modifying smart contract state.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    5.9
   </td>
   <td colspan="2" >
    Certify that critical roles in the decentralized application are not managed by a single user. 
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    5.10
   </td>
   <td colspan="2" >
    The transaction sender should be validated using the correct means only.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    5.11
   </td>
   <td colspan="2" >
    Access control mechanisms should be thoroughly tested according to specifications and free from vulnerabilities.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    5.12
   </td>
   <td colspan="2" >
    When implementing an off-chain authentication mechanism on smart contracts, ensure the implementation follows a standardized and widely tested one.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    5.13
   </td>
   <td colspan="2" >
    Prevent smart contract roles having elevated privileges (such as mint, transfer, change ownership,etc  …) to be associated with an External Owner Address (EOA).
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    5.14
   </td>
   <td colspan="2" >
    Verify all modifiers' logic are simple and use the correct mechanisms to perform input validation. 
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    5.15
   </td>
   <td colspan="2" >
    Verify that any change in access control configuration should follow an internal well-defined process. 
   </td>
   <td>Medium
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    5.16
   </td>
   <td colspan="2" >
    The access control mechanism of a large decentralized application should be centralized for better control.
   </td>
   <td>Low
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    5.17
   </td>
   <td colspan="2" >
    Describe and document any existing time lock mechanism and its purpose.
   </td>
   <td>Low
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>6</strong>
   </td>
   <td colspan="5" >
    <strong><em>Business Logic</em></strong>
   </td>
  </tr>
  <tr>
   <td>
    6.1
   </td>
   <td colspan="2" >
    Ensure the logic of the smart contract does not assume it cannot receive infrastructure tokens.
   </td>
   <td>Medium
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    6.2
   </td>
   <td colspan="5" >
    <strong>Front Running</strong>
   </td>
  </tr>
  <tr>
   <td>
    6.2.1
   </td>
   <td colspan="2" >
    To prevent front-running in a Dapp, and protect users, ensure that one of the following solutions is in place: Preventing time and order to have to influence the outcome of the transaction, using a pre-commit scheme, or limiting the benefits a front-runner could have.
   </td>
   <td>Medium
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    6.3
   </td>
   <td colspan="5" >
    <strong>Denial of Service</strong>
   </td>
  </tr>
  <tr>
   <td>
    6.3.1
   </td>
   <td colspan="2" >
    Ensure that Dapp logic cannot be impacted by Dos attacks such as block stuffing, where an attacker prevents other transactions from being validated over a certain period of time.
   </td>
   <td>Medium
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>7</strong>
   </td>
   <td colspan="5" >
    <strong><em>Utility Tokens</em></strong>
   </td>
  </tr>
  <tr>
   <td>
    <strong>7.1</strong>
   </td>
   <td colspan="5" >
    <strong>General</strong>
   </td>
  </tr>
  <tr>
   <td>
    7.1.1
   </td>
   <td colspan="2" >
    Tokens need to meet the corresponding specification standards. Use existing standards that have been widely tested.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    7.1.2
   </td>
   <td colspan="2" >
    Project administrators should not have high-authority functions to operate user token assets.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    7.1.3
   </td>
   <td colspan="2" >
    Ensure decentralized applications only request user token approval for the exact amount of tokens the user wants to transfer. 
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    7.1.4
   </td>
   <td colspan="2" >
    The token handling fee should have a reasonable range, rather than potentially being modified arbitrarily by the administrator.
   </td>
   <td>Medium
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>7.2</strong>
   </td>
   <td colspan="5" >
    <strong>Reflection Token</strong>
   </td>
  </tr>
  <tr>
   <td>
    7.2.1
   </td>
   <td colspan="2" >
    Validate that the rate calculation mechanism of the token is done safely. The token handling fee should have a reasonable range, rather than being arbitrarily specified by the administrator.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>8</strong>
   </td>
   <td colspan="5" >
    <strong><em>Code Clarity</em></strong>
   </td>
  </tr>
  <tr>
   <td>
    8.1
   </td>
   <td colspan="2" >
    Certify the developers are using the recent stable version of the compiler.
   </td>
   <td>
    High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    8.2
   </td>
   <td colspan="2" >
    Ensure that modifications to pertinent smart contract state variables activate corresponding events and certify their functionality. 
   </td>
   <td>Medium
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    8.3
   </td>
   <td colspan="2" >
    All storage variables should be initialized.
   </td>
   <td>Medium
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    8.4
   </td>
   <td colspan="2" >
    Clearly define the smart contract variables' location as storage, memory, or calldata.
   </td>
   <td>Medium
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    8.5
   </td>
   <td colspan="2" >
    Verify that the smart contracts code makes the distinction between trusted(owned smart contracts) and untrusted (3rd party) smart contracts.
   </td>
   <td>Medium
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    8.6
   </td>
   <td colspan="2" >
    Certify that assembly low-level code is only used if necessary and is properly commented on and documented.
   </td>
   <td>Low
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    8.7
   </td>
   <td colspan="2" >
    Certify that unchecked code is clearly commented on following industry standards and documented.
   </td>
   <td>Low
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    8.8
   </td>
   <td colspan="2" >
    For the developer's readability, ensure technical documentation in the contract.
   </td>
   <td>Low
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    8.9
   </td>
   <td colspan="2" >
    Avoid using functions and variables with similar names.
   </td>
   <td>Low
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    8.10
   </td>
   <td colspan="2" >
    Logic should be clear and kept in simple modular contracts and functions.
   </td>
   <td>Low
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    8.11
   </td>
   <td colspan="2" >
    Clean unused variables and functions 
   </td>
   <td>Low
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    8.12
   </td>
   <td colspan="2" >
    The inheritance order for contracts should be defined and documented to prevent bugs using multiple inheritance or shadow functions.
   </td>
   <td>Low
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    8.13
   </td>
   <td colspan="2" >
    Certifying the code annotation matches the code implementation. 
   </td>
   <td>Low
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    8.14
   </td>
   <td colspan="2" >
    Verify that the same rules for variable naming are followed throughout all the contracts (e.g. use the same variable name for the same object).
   </td>
   <td>Low
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    <strong>9</strong>
   </td>
   <td colspan="5" >
    <strong><em>Education and Training</em></strong>
   </td>
  </tr>
  <tr>
   <td>
    9.1
   </td>
   <td colspan="2" >Provide team members with regular training around smart contract security and best practices.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    9.2
   </td>
   <td colspan="2" >Maintain internal documentation of best practices to be followed by team members and new joiners.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
  <tr>
   <td>
    9.3
   </td>
   <td colspan="2" >Ensure team members are fully aware of phishing, ice phishing, social engineering attacks, and new techniques of scams.
   </td>
   <td>High
   </td>
   <td>
<ol>

<input type="checkbox">
</ol>
   </td>
   <td>
   </td>
  </tr>
</table>
