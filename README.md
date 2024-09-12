# Law Search Aggregator

## Project Overview

This project aimed to automate the process of retrieving results from various law research platforms, such as Dalloz, to ease the burden of manually searching through multiple legal databases. By automating this process, users could search once and gather results from multiple platforms, saving time and avoiding the need to navigate each platform individually.

### Motivation

Legal research often involves searching across multiple databases and platforms, each with different interfaces and access methods. This project was designed to streamline that process by logging into the required platforms, submitting a query, and collecting the results into a single, unified search. It was intended to help legal professionals, students, or researchers reduce the repetitive and time-consuming tasks of individually accessing each platform.

I did that because I feel this pain so many times during my law studies and intership while also having a big interest in this kind of hacking solution

## Technologies Used

- **Selenium WebDriver**: To automate browser interactions and simulate user inputs (e.g., logging in, navigating, searching).
- **Python**: Used for scripting and handling the automation logic.
- **ChromeDriver**: The Chrome-specific WebDriver used for browser automation.

## How It Works

1. **Login Automation**: 
   - The script automates the login process to Paris 1 University's platforms using credentials provided by the user.
   
2. **Platform Navigation**: 
   - Once logged in, the script navigates through multiple layers of the website, clicking through to specific law libraries such as Mikado and Domino.

3. **Search Functionality**: 
   - After accessing the relevant legal databases, the script submits search queries (e.g., "Droit pénal") to retrieve the results.

4. **Result Extraction**: 
   - The script captures the resulting search items, prints the inner HTML of each result, and was intended to store or process these results further.

## Challenges and Reason for Stopping the Project

Although the initial goal of automating legal search across platforms was technically feasible, the project was halted due to the numerous edge cases and variabilities across different platforms. Some challenges included:

- **Platform Differences**: Each platform had unique layouts, search mechanisms, and access restrictions, which made it difficult to create a universal solution.
- **Login and Access Mechanisms**: Some platforms required special authentication steps or specific permissions, adding complexity to the automation.
- **Dynamic Content and Delays**: Handling different types of loading mechanisms (e.g., AJAX, JavaScript-based dynamic content) was complex, requiring customized logic for each platform.
  
Ultimately, the maintenance and scalability of handling all these different cases proved too burdensome.

### README.md proudly make with chatGPT ❤️❤️❤️❤️
