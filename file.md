## Looker Explore Deprecation Process

This document outlines the process our team follows when deprecating Looker explores.

Goals:

- Communicate upcoming explore deprecation to users.
- Minimize disruption to users who rely on the explore.
- Encourage users to adopt alternative explores.

## Process:

1. Initiate Deprecation:

    - Identify the explore to be deprecated.
    - Define a deprecation timeline with a clear end date (e.g., 3 months from initiation).

2. Update Explore Name:

    - Rename the explore to explicitly state its upcoming deprecation and end date.
    - Example: "[DEPRECATED as of YYYY-MM-DD] - Original Explore Name"

3. Identify Explore Users:

    - Use Looker tools (Explore usage statistics) to identify users who have accessed the explore recently.

4. Identify Dependent Reports:

    - Analyze dashboards and Looks to identify reports currently using the explore.

5. Communication:

    - Announce Deprecation:
        - Send a Slack message to relevant channels (e.g., #looker-announcements) explaining:
        - The explore to be deprecated and its end date.
        - The reason for deprecation (optional).
        - The impact on existing reports (optional).
    - Offer Alternatives:
        - Recommend alternative explores (if available) with a brief explanation of their functionalities.
        - Provide migration guidance if necessary (complex reports).

6. Post-Deprecation:

    - Consider archiving or hiding the deprecated explore after the end date.
    - Monitor for any unexpected issues related to the deprecation.
