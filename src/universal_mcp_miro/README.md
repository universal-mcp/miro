# Universal Mcp Miro MCP Server

An MCP Server for the Universal Mcp Miro API.

## 📋 Prerequisites

Before you begin, ensure you have met the following requirements:
* Python 3.11+ (Recommended)
* [uv](https://github.com/astral-sh/uv) installed globally (`pip install uv`)

## 🛠️ Setup Instructions

Follow these steps to get the development environment up and running:

### 1. Sync Project Dependencies
Navigate to the project root directory (where `pyproject.toml` is located).
```bash
uv sync
```
This command uses `uv` to install all dependencies listed in `pyproject.toml` into a virtual environment (`.venv`) located in the project root.

### 2. Activate the Virtual Environment
Activating the virtual environment ensures that you are using the project's specific dependencies and Python interpreter.
- On **Linux/macOS**:
```bash
source .venv/bin/activate
```
- On **Windows**:
```bash
.venv\\Scripts\\activate
```

### 3. Start the MCP Inspector
Use the MCP CLI to start the application in development mode.
```bash
mcp dev src/universal_mcp_miro/mcp.py
```
The MCP inspector should now be running. Check the console output for the exact address and port.

## 🔌 Supported Integrations

- AgentR
- API Key (Coming Soon)
- OAuth (Coming Soon)

## 🛠️ Tool List

This is automatically generated from OpenAPI schema for the Universal Mcp Trello API.


Here is the markdown table summarizing the tools in the `MiroApp` class:

| Tool | Description |
|------|-------------|
| `revoke_token_v1` | Revokes the provided access token, making it no longer valid, along with any associated refresh token. |
| `get_access_token_information` | Get detailed information about an access token, including token type, scopes, team, user, and creation details. |
| `get_audit_logs` | Retrieves a paginated list of audit logs within a specified time range, supporting cursor-based pagination. |
| `get_organization_settings` | Retrieve organization settings including board classification configurations. Intended for Enterprise plan users with Company Admin role. |
| `bulk_update_boards_classification` | Bulk updates board classification for either not-classified boards only or all boards in a team, depending on the provided parameters. |
| `get_team_settings` | Retrieves board classification settings for an existing team. Requires enterprise-level access and company admin privileges. |
| `update_team_settings` | Updates team settings, specifically board classification settings for an existing team. |
| `get_board_classification` | Retrieve board classification details for an associated board. This endpoint is restricted to Enterprise plan users with Company Admin privileges. |
| `update_board_classification` | Updates the classification label for an existing board by modifying its label ID. |
| `get_all_cases` | Retrieves a paginated list of eDiscovery cases in an organization, supporting cursor-based pagination. |
| `get_case` | Retrieves case information from the organization, including details relevant to legal holds. |
| `get_all_legal_holds_within_acase` | Retrieves a paginated list of all legal holds within a case for an organization, supporting cursor-based pagination. |
| `get_legal_hold_information` | Retrieve legal hold information for a case within an organization. |
| `get_content_items_under_legal_hold` | Fetches content items under legal hold for review or exploration purposes. |
| `create_board_export_job` | Creates an export job for one or more boards using the specified format and identifiers. |
| `get_board_export_job_status` | Retrieve the status of a board export job, including completion state and any relevant metadata. |
| `get_results_for_board_export_job` | Retrieves the results of a board export job, providing information such as the S3 link to exported files. |
| `retrieve_content_change_logs_of_board_items` | Retrieve content change logs for board items, including actions like updates and deletions, filtered by boards, users, and time range with pagination support. |
| `reset_all_sessions_of_auser` | Reset all active sessions for a specified user, requiring them to sign in again across all devices. |
| `get_organization_info` | Retrieves organization information from the Miro API, including details available only to Enterprise plan users with Company Admin role. |
| `get_organization_members` | Retrieves organization members based on specified criteria like emails or cursor. |
| `get_organization_member` | Retrieves organization member information from the Miro API with Company Admin permissions. |
| `get_boards` | Retrieves a list of boards accessible to the user, allowing filtering by team, project, and other parameters. |
| `copy_board` | Creates a copy of an existing board, allowing updates to name, description, sharing policy, and permissions policy. |
| `create_board` | Creates a new board with specified attributes and sharing policies. |
| `get_specific_board` | Retrieves information about a specific board from the Miro API. |
| `delete_board` | Deletes a board, moving it to the trash where it can be restored within 90 days. |
| `update_board` | Updates a specific board by modifying its description, name, policy, project ID, or team ID. |
| `create_app_card_item` | Creates an app card item and adds it to a Miro board, constructing the request from provided parameters. |
| `get_app_card_item` | Retrieves information for a specific app card item on a Miro board. |
| `delete_app_card_item` | Deletes an app card item from a board, requiring the boards:write scope and subject to rate limiting at Level 3. |
| `update_app_card_item` | Updates an app card item's properties including data, geometry, parent relationship, position, and style on a Miro board. |
| `create_card_item` | Creates a new card item and adds it to a Miro board with specified properties. |
| `get_card_item` | Retrieves information for a specific card item on a board |
| `delete_card_item` | Deletes a card item from the Miro board. |
| `update_card_item` | Updates a card item on a board based on the provided data and style properties. |
| `get_connectors` | Retrieves a list of connectors for a specific board using a cursor-based approach. |
| `create_connector` | Creates a connector on a board by sending a POST request with specified parameters. |
| `get_specific_connector` | Retrieves information for a specific connector on a board. |
| `delete_connector` | Error generating docstring |
| `update_connector` | Updates a connector's properties on a board including captions, end/start items, shape, and style. |
| `create_document_item_using_url` | Create a document item on a board using a URL, adding it with specified data, geometry, position, and parent relationships. |
| `get_document_item` | Retrieves information for a specific document item from a Miro board. |
| `delete_document_item` | Deletes a document item from the board, requiring a specific scope and rate limit tier. |
| `update_document_item_using_url` | Updates a document item using a URL by sending a PATCH request with the provided data, geometry, parent, and position. |
| `create_document_item_using_file_from_device` | Creates a document item on a board by uploading a file from the user's device. |
| `update_document_item_using_file_from_device` | Updates a document item on a Miro board using a file from a connected device. |
| `create_embed_item` | Creates an embed item to add external content to a Miro board. |
| `get_embed_item` | Retrieves information for a specific embed item on a board. |
| `delete_embed_item` | Delete an embed item from a board. |
| `update_embed_item` | Updates an embed item on a Miro board with specified properties, including data, geometry, parent relationships, and positioning. |
| `create_image_item_using_url` | Creates an image item on a Miro board using a URL, adding the image to the board with specified data and positioning. |
| `get_image_item` | Retrieves information for a specific image item on a board. |
| `delete_image_item` | Deletes an image item from the board. |
| `update_image_item_using_url` | Updates an image item on a Miro board using URL, modifying its data, geometry, parent, or position. |
| `create_image_item_using_file_from_device` | Creates an image item in a board by uploading a file from the device. |
| `update_image_item_using_file_from_device` | Updates an image item on a Miro board using a file from the user's device |
| `get_items_on_board` | Retrieves items from a specific board using cursor-based pagination. |
| `get_specific_item_on_board` | Retrieves information for a specific item on a board. |
| `delete_item` | Deletes an item from a board, requiring specific permissions and adhering to rate limiting policies. |
| `update_item_position_or_parent` | Updates the position or the parent of an item on a board. |
| `get_items_within_frame` | Retrieves a list of items within a specific frame using a cursor-based approach. |
| `get_specific_item_on_board1` | Retrieves information for a specific item on a board from the Miro API, requiring read access to board data. |
| `delete_item1` | Deletes an item from the board. |
| `get_all_board_members` | Retrieves a pageable list of all members for a board with optional pagination using limit and offset parameters. |
| `share_board` | Shares a board and invites new members by sending an invitation email based on provided parameters. |
| `get_specific_board_member` | Retrieves information for a specific board member. |
| `remove_board_member` | Removes a board member from a board. |
| `update_board_member` | Updates the role of a specific board member by submitting a PATCH request with the new role. |
| `create_shape_item` | Creates a shape item on a board with specified properties and optional components. |
| `get_shape_item` | Retrieve information for a specific shape item on a board. |
| `delete_shape_item` | Deletes a shape item from the board. |
| `update_shape_item` | Updates a shape item on a board based on the provided data, geometry, parent, position, and style. |
| `create_sticky_note_item` | Creates a sticky note item on a Miro board with specified properties. |
| `get_sticky_note_item` | Retrieves information for a specific sticky note item on a Miro board. |
| `delete_sticky_note_item` | Deletes a sticky note item from the board. |
| `update_sticky_note_item` | Updates a sticky note item on a board based on provided data and style properties. |
| `create_text_item` | Creates a text item on a board by sending a POST request with the specified parameters. |
| `get_text_item` | Retrieves information for a specific text item on a Miro board, requiring boards:read scope and subject to rate limiting. |
| `delete_text_item` | Deletes a text item from a board, requiring specific permissions and adhering to rate limiting rules. |
| `update_text_item` | Updates a text item on a board based on the provided data and style properties. |
| `create_items_in_bulk` | Creates items in bulk by adding up to 20 items of the same or different types to a board in a single transactional operation |
| `create_items_in_bulk_using_file_from_device` | Create items in bulk using a file from a device. |
| `create_frame` | Creates a new frame on a board by sending the provided data, geometry, position, and style. |
| `get_frame` | Retrieves information for a specific frame on a Miro board. |
| `delete_frame` | Delete a frame from a Miro board. |
| `update_frame` | Updates a frame on a board using the provided data, style, geometry, or position properties. |
| `get_app_metrics` | Fetches app metrics for a specified time range and groups data by given period. |
| `get_total_app_metrics` | Get total usage metrics for a specific app since its creation. |
| `create_webhook_subscription` | Creates a webhook subscription to receive item-update notifications for a specified Miro board. |
| `update_webhook_subscription` | Updates the status or callback URL of an existing webhook subscription. |
| `get_webhook_subscriptions` | Retrieves information about webhook subscriptions for a user. |
| `get_specific_webhook_subscription` | Retrieves information for a specific webhook subscription from the Miro API. |
| `delete_webhook_subscription` | Deletes the specified webhook subscription. |
| `get_specific_mind_map_node` | Retrieves information for a specific mind map node on a Miro board, requiring boards:read scope. |
| `delete_mind_map_node` | Error generating docstring |
| `get_mind_map_nodes` | Retrieve mind map nodes using cursor-based pagination for a specific board. |
| `create_mind_map_node` | Create a mind map node, adding it to a board as either a root node or a child node under another node. |
| `get_items_on_board1` | Retrieve paginated items from a specific board using cursor-based pagination, with optional filtering by item type. |
| `create_shape_item1` | Creates a flowchart shape item on a Miro board using the provided parameters. |
| `get_shape_item1` | Retrieves information for a specific shape item on a board. |
| `delete_shape_item1` | Deletes a flowchart shape item from the board. |
| `update_shape_item1` | Updates a flowchart shape item on a board based on the provided data and style properties. |
| `get_all_groups_on_aboard` | Retrieves all groups on a board, using a cursor-based pagination approach. |
| `create_group` | Creates a group of items on a Miro board using the provided data dictionary. |
| `get_items_of_agroup_by_id` | Retrieves items of a group by ID using a cursor-based approach. |
| `get_agroup_by_its_id` | Failed to extract docstring information |
| `updates_agroup_with_new_items` | Updates an existing group entirely by replacing it with new data and assigns a new group ID. |
| `ungroup_items` | Ungroups items from a group, optionally deleting them. |
| `deletes_the_group` | Deletes a group from the board, optionally removing items within it. |
| `revoke_token_v2` | Revoke an access token and its associated refresh token, invalidating them immediately and preventing further use. |
| `get_tags_from_item` | Retrieves all tags associated with the specified item by making a GET request to the Miro API endpoint. |
| `get_tags_from_board` | Retrieves tags from a specified board using pagination parameters. |
| `create_tag` | Creates a tag on a board with specified visual attributes, requiring API write access. |
| `get_tag` | Retrieves information for a specific tag from the Miro API, requiring the 'boards:write' scope. |
| `delete_tag` | Deletes a specified tag from the board, removing it from all cards and sticky notes. |
| `update_tag` | Updates a tag's properties (fill color and title) on a Miro board. |
| `get_items_by_tag` | Retrieves items associated with a specified tag from a Miro board. |
| `attach_tag_to_item` | Attaches an existing tag to a specified Miro board item (card or sticky note). |
| `remove_tag_from_item` | Removes a specific tag from an item without deleting the tag itself. |
| `list_of_projects` | Retrieves a list of projects in an organization, including private projects with Content Admin permissions. |
| `create_project` | Creates a new project in an existing team as an organizational container for boards, enabling shared access management. |
| `get_project` | Retrieves project information, such as the name of an existing project. |
| `delete_project` | Deletes a project, retaining associated boards and users within the team. |
| `update_project` | Updates project information, including the project name. |
| `get_project_settings` | Retrieves project settings from the Miro API. |
| `update_project_settings` | Updates the settings of a project, specifically modifying the sharing policy settings. |
| `list_of_project_members` | Retrieves a paginated list of members for a specific project, supporting cursor-based pagination. |
| `add_member_in_aproject` | Adds a member to a project by sending a request with the member's email and role. |
| `get_project_member` | Retrieves information for a specific project member from Miro. |
| `remove_project_member` | Remove a project member from a project without removing them from the team. |
| `update_project_member` | Updates the role of a project member. |
| `list_teams` | Retrieves a paginated list of teams in an organization, filtered by name if provided. |
| `create_team` | Creates a new team in an existing organization with the specified name. |
| `get_team` | Retrieves team information for an existing team, available for Enterprise plan users. |
| `delete_team` | Delete an existing team from the Miro organization, requiring Company Admin privileges and Enterprise plan access. |
| `update_team` | Updates an existing team by changing its name. |
| `list_team_members` | Retrieves team members with pagination and optional role filtering, requiring specific permissions and rate limits. |
| `invite_team_members` | Invites a new Miro user to an existing team via email, requiring the user to exist in the organization. |
| `get_team_member` | Retrieves a team member. |
| `delete_team_member_from_team` | Deletes a team member from a team. |
| `update_team_member` | Updates the role of a team member within an organization, requiring Company Admin permissions and a specific scope. |
| `get_default_team_settings` | Retrieve default team settings for an existing organization. |
| `get_team_settings1` | Retrieves team settings for an existing team. |
| `update_team_settings1` | Updates team settings for an existing team. |
## 📁 Project Structure

The generated project has a standard layout:
```
.
├── src/                  # Source code directory
│   └── universal_mcp_miro/
│       ├── __init__.py
│       └── mcp.py        # Server is launched here
│       └── app.py        # Application tools are defined here
├── tests/                # Directory for project tests
├── .env                  # Environment variables (for local development)
├── pyproject.toml        # Project dependencies managed by uv
├── README.md             # This file
```

## 📝 License

This project is licensed under the MIT License.

---

_This project was generated using **MCP CLI** — Happy coding! 🚀_

## Usage

- Login to AgentR
- Follow the quickstart guide to setup MCP Server for your client
- Visit Apps Store and enable the Universal Mcp Trello app
- Restart the MCP Server

### Local Development

- Follow the README to test with the local MCP Server 