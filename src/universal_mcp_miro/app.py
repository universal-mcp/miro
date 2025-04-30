from typing import Any, Annotated
from universal_mcp.applications import APIApplication
from universal_mcp.integrations import Integration

class MiroApp(APIApplication):
    def __init__(self, integration: Integration = None, **kwargs) -> None:
        super().__init__(name='miro', integration=integration, **kwargs)
        self.base_url = "https://api.miro.com"


    def revoke_token_v1(self, access_token: Annotated[Any, '(Required) Access token that you want to revoke'] = None) -> Any:
        """
        Revokes the provided access token, making it no longer valid, along with any associated refresh token.
        
        Args:
            access_token: (Optional) The access token to be revoked. If not provided, no token is revoked. Type: Any
        
        Returns:
            The JSON response from the server after revoking the access token. Returns None if no data is returned.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            revoke, token, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "access_token": access_token,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_access_token_information(self, ) -> Any:
        """
        Get detailed information about an access token, including token type, scopes, team, user, and creation details.
        
        Args:
            None: No parameters required.
        
        Returns:
            A JSON response containing access token details.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            access, tokens, information, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_audit_logs(self, createdAfter: Annotated[Any, '(Required) Retrieve audit logs created after the date and time provided. This is the start date of the duration for which you want to retrieve audit logs. For example, if you want to retrieve audit logs between `2023-03-30T17:26:50.000Z` and `2023-04-30T17:26:50.000Z`, provide `2023-03-30T17:26:50.000Z` as the value for the `createdAfter` parameter.<br>Format: UTC, adheres to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601), including milliseconds and a [trailing Z offset](https://en.wikipedia.org/wiki/ISO_8601#Coordinated_Universal_Time_(UTC))."\n'] = None, createdBefore: Annotated[Any, '(Required) Retrieve audit logs created before the date and time provided. This is the end date of the duration for which you want to retrieve audit logs. For example, if you want to retrieve audit logs between `2023-03-30T17:26:50.000Z` and `2023-04-30T17:26:50.000Z`, provide `2023-04-30T17:26:50.000Z` as the value for the `createdBefore` parameter.<br>Format: UTC, adheres to [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601), including milliseconds and a [trailing Z offset](https://en.wikipedia.org/wiki/ISO_8601#Coordinated_Universal_Time_(UTC)).\n'] = None, cursor: Annotated[Any, 'A cursor-paginated method returns a portion of the total set of results based on the `limit` specified and a `cursor` that points to the next portion of the results. To retrieve the next set of results of the collection, set the `cursor` parameter in your next request to the appropriate cursor value returned in the response.'] = None, limit: Annotated[Any, 'Maximum number of results returned based on the `limit` specified in the request. For example, if there are `30` results, the request has no `cursor` value, and the `limit` is set to `20`,the `size` of the results will be `20`. The rest of the results will not be returned. To retrieve the rest of the results, you must make another request and set the appropriate value for the `cursor` parameter value that  you obtained from the response.<br>Default: `100`\n'] = None, sorting: Annotated[Any, 'Sort order in which you want to view the result set. Based on the value you provide, the results are sorted in an ascending or descending order of the audit log creation date (audit log `createdAt` parameter).<br>Default: `ASC`\n'] = None) -> Any:
        """
        Retrieves a paginated list of audit logs within a specified time range, supporting cursor-based pagination.
        
        Args:
            createdAfter: Earliest timestamp for audit logs (inclusive). Must be ISO 8601 UTC format with milliseconds and trailing 'Z' (e.g., '2023-03-30T17:26:50.000Z').
            createdBefore: Latest timestamp for audit logs (exclusive). Must be ISO 8601 UTC format with milliseconds and trailing 'Z' (e.g., '2023-04-30T17:26:50.000Z').
            cursor: Pagination cursor token for subsequent requests.
            limit: Maximum number of results per page (default: 100).
            sorting: Sort order for results ('ASC' or 'DESC' by creation date, default: 'ASC').
        
        Returns:
            JSON response containing audit logs and pagination metadata.
        
        Raises:
            HTTPError: When request fails due to invalid parameters, authentication issues, or server errors.
        
        Tags:
            audit-logs, paginated, async-job, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "createdAfter": createdAfter,
                "createdBefore": createdBefore,
                "cursor": cursor,
                "limit": limit,
                "sorting": sorting,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_organization_settings(self, ) -> Any:
        """
        Retrieve organization settings including board classification configurations. Intended for Enterprise plan users with Company Admin role.
        
        Returns:
            Dictionary containing organization settings data from the API response
        
        Raises:
            HTTPError: If the API request fails due to network issues, authentication errors, or invalid permissions
        
        Tags:
            retrieve, organization-settings, enterprise, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def bulk_update_boards_classification(self, labelId: Annotated[float, ''] = None, notClassifiedOnly: Annotated[bool, ''] = None) -> Any:
        """
        Bulk updates board classification for either not-classified boards only or all boards in a team, depending on the provided parameters.
        
        Args:
            labelId: The ID of the label to apply for classification. Defaults to None.
            notClassifiedOnly: A flag indicating whether to classify only not-classified boards. Defaults to None.
        
        Returns:
            The response from the server as JSON.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            classification, bulk-update, boards, management, important
        """
        request_body = {
            "labelId": labelId,
            "notClassifiedOnly": notClassifiedOnly,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_team_settings(self, ) -> Any:
        """
        Retrieves board classification settings for an existing team. Requires enterprise-level access and company admin privileges.
        
        Returns:
            Parsed JSON response containing team-level board classification settings.
        
        Raises:
            requests.exceptions.HTTPError: If the API request fails due to invalid permissions, rate limits, or server errors (4xx/5xx status codes).
        
        Tags:
            retrieve, team-settings, board-classification, enterprise, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_team_settings(self, defaultLabelId: Annotated[float, ''] = None, enabled: Annotated[bool, ''] = None) -> Any:
        """
        Updates team settings, specifically board classification settings for an existing team.
        
        Args:
            defaultLabelId: Optional float specifying the default label ID.
            enabled: Optional boolean indicating whether the setting is enabled.
        
        Returns:
            A JSON response from the server after updating the team settings.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            update, team, settings, board-classification, enterprise, important
        """
        request_body = {
            "defaultLabelId": defaultLabelId,
            "enabled": enabled,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_board_classification(self, ) -> Any:
        """
        Retrieve board classification details for an associated board. This endpoint is restricted to Enterprise plan users with Company Admin privileges.
        
        Args:
            None: This method does not accept parameters
        
        Returns:
            Response dictionary containing board classification data as returned by the Miro API
        
        Raises:
            requests.exceptions.HTTPError: Raised for 4XX/5XX HTTP status codes when the API request fails, including invalid permissions or rate limits
            ValueError: Raised if API response contains malformed JSON data
        
        Tags:
            board-classification, enterprise, api, important, board-management
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_board_classification(self, labelId: Annotated[Any, ''] = None) -> Any:
        """
        Updates the classification label for an existing board by modifying its label ID.
        
        Args:
            labelId: (Any) Identifier of the classification label to apply. Use None to remove existing classification.
        
        Returns:
            Dict[str, Any]: Parsed JSON response containing the updated board details.
        
        Raises:
            HTTPError: If server returns 4XX/5XX status code during API request, with specifics determined by Miro's API error responses.
        
        Tags:
            update, board-classification, management, important, async_job
        """
        request_body = {
            "labelId": labelId,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_cases(self, cursor: Annotated[Any, 'An indicator of the position of a page in the full set of results. To obtain the first page leave it empty. To obtain subsequent pages set it to the value returned in the cursor field of the previous request.\n'] = None, limit: Annotated[Any, '(Required) The maximum number of items in the result list.'] = None) -> Any:
        """
        Retrieves a paginated list of eDiscovery cases in an organization, supporting cursor-based pagination.
        
        Args:
            cursor: An indicator of pagination position. Leave empty for first page, use returned cursor from previous request for subsequent pages.
            limit: Maximum number of items to return in the result list (required for pagination).
        
        Returns:
            Response JSON containing paginated case results and next cursor position.
        
        Raises:
            HTTPError: When the API request fails, indicated by non-2xx status codes.
        
        Tags:
            list, pagination, legal-holds, ediscovery, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "cursor": cursor,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_case(self, ) -> Any:
        """
        Retrieves case information from the organization, including details relevant to legal holds. This function requires specific permissions and is only available to Enterprise Guard users with both Company Admin and eDiscovery Admin roles.
        
        Args:
            : None
        
        Returns:
            A dictionary containing case details retrieved from the API response.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the API request fails due to unauthorized access, invalid parameters, or server-side issues.
        
        Tags:
            legal-holds, case-management, enterprise-guard, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_legal_holds_within_acase(self, cursor: Annotated[Any, 'An indicator of the position of a page in the full set of results. To obtain the first page leave it empty. To obtain subsequent pages set it to the value returned in the cursor field of the previous request.\n'] = None, limit: Annotated[Any, '(Required) The maximum number of items in the result list.'] = None) -> Any:
        """
        Retrieves a paginated list of all legal holds within a case for an organization, supporting cursor-based pagination.
        
        Args:
            cursor: An indicator of the position of a page in the full set of results. Leave empty to retrieve the first page. Provide the cursor value from the previous response to fetch subsequent pages.
            limit: (Required) The maximum number of items to include in the result list.
        
        Returns:
            A parsed JSON response containing the list of legal holds and pagination metadata.
        
        Raises:
            HTTPError: If the API request fails due to network issues, authentication errors, or invalid parameters.
        
        Tags:
            legal-holds, pagination, list, async-job, important, ediscovery, management
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "cursor": cursor,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_legal_hold_information(self, ) -> Any:
        """
        Retrieve legal hold information for a case within an organization.
        
        Args:
            None: This function takes no parameters.
        
        Returns:
            A JSON object containing legal hold information.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request encounters an error (e.g., server returns a 4xx or 5xx status code).
        
        Tags:
            legal-hold, management, organization, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_content_items_under_legal_hold(self, cursor: Annotated[Any, 'An indicator of the position of a page in the full set of results. To obtain the first page leave it empty. To obtain subsequent pages set it to the value returned in the cursor field of the previous request.\n'] = None, limit: Annotated[Any, '(Required) The maximum number of items in the result list.'] = None) -> Any:
        """
        Fetches content items under legal hold for review or exploration purposes.
        
        Args:
            cursor: An indicator of the position of a page in the full set of results. To obtain the first page, leave it empty. To obtain subsequent pages, set it to the value returned in the cursor field of the previous request.
            limit: The maximum number of items in the result list.
        
        Returns:
            A list of content items under a specific legal hold.
        
        Raises:
            HTTPError: Raised if there is an HTTP-level error during the request.
        
        Tags:
            review, legal-hold, management, important, enterprise
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "cursor": cursor,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_board_export_job(self, boardFormat: Annotated[Any, ''] = None, boardIds: Annotated[list[Any], ''] = None, request_id: Annotated[Any, '(Required) Unique identifier of the board export job.'] = None) -> Any:
        """
        Creates an export job for one or more boards using the specified format and identifiers.
        
        Args:
            boardFormat: Optional format for the board export.
            boardIds: Optional list of IDs of boards to export.
            request_id: Unique identifier for the board export job, required for tracking purposes.
        
        Returns:
            JSON response from the successful creation of a board export job.
        
        Raises:
            requests.RequestException: Raised if there is a problem with the HTTP request, such as connection issues or invalid responses.
        
        Tags:
            export, job, board, async_job, enterprise, management, important
        """
        request_body = {
            "boardFormat": boardFormat,
            "boardIds": boardIds,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "request_id": request_id,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_board_export_job_status(self, ) -> Any:
        """
        Retrieve the status of a board export job, including completion state and any relevant metadata.
        
        Args:
            None: This function takes no parameters.
        
        Returns:
            A JSON response containing the job status details and metadata, typically including fields like 'status', 'createdAt', and 'downloadUrl'.
        
        Raises:
            HTTPError: Raised for failed API requests (4xx/5xx responses)
            JSONDecodeError: Raised if the response body contains invalid JSON
        
        Tags:
            retrieve, status-check, board-export, async-job, enterprise, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_results_for_board_export_job(self, ) -> Any:
        """
        Retrieves the results of a board export job, providing information such as the S3 link to exported files.
        
        Args:
            None: This function does not accept any parameters.
        
        Returns:
            The result of the board export job in JSON format.
        
        Raises:
            requests.HTTPError: Raised if an HTTP request returns an unsuccessful status code.
        
        Tags:
            export, enterprise, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def retrieve_content_change_logs_of_board_items(self, board_ids: Annotated[Any, 'List of board IDs for which you want to retrieve the content logs.'] = None, cursor: Annotated[Any, 'A cursor-paginated method returns a portion of the total set of results based on the limit specified and a cursor that points to the next portion of the results. To retrieve the next portion of the collection, set the cursor parameter equal to the cursor value you received in the response of the previous request.\n'] = None, emails: Annotated[Any, 'Filter content logs based on the list of emails of users who created, modified, or deleted the board item.'] = None, limit: Annotated[Any, 'The maximum number of results to return per call. If the number of logs in the response is greater than the limit specified, the response returns the cursor parameter with a value.\n'] = None, sorting: Annotated[Any, 'Sort order in which you want to view the result set based on the modified date. To sort by an ascending modified date, specify `asc`. To sort by a descending modified date, specify `desc`.\n'] = None, to: Annotated[Any, '(Required) Filter content logs based on the date and time when the board item was last modified. This is the end date and time for the modified date duration. Format: UTC, adheres to\n[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601), includes a [trailing Z offset](https://en.wikipedia.org/wiki/ISO_8601#Coordinated_Universal_Time_(UTC)).\n'] = None) -> Any:
        """
        Retrieve content change logs for board items, including actions like updates and deletions, filtered by boards, users, and time range with pagination support.
        
        Args:
            board_ids: List of board IDs for which to retrieve content logs. Multiple IDs can be specified.
            cursor: Cursor for pagination. Use the value from previous response to retrieve next results.
            emails: Filter logs by email addresses of users who modified board items.
            limit: Maximum number of logs to return per request. Pagination required if exceeded.
            sorting: Sort order by modification date: 'asc' for ascending or 'desc' for descending.
            to: End datetime for filtering modified items (UTC ISO 8601 format with trailing Z). Required parameter.
        
        Returns:
            Response JSON containing paginated content change logs and cursor for subsequent requests.
        
        Raises:
            requests.HTTPError: Raised for API request failures such as invalid parameters, authentication errors, or when the required scope is missing.
        
        Tags:
            retrieve, logs, board, paginated, enterprise, content-management, async_job, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "board_ids": board_ids,
                "emails": emails,
                "to": to,
                "cursor": cursor,
                "limit": limit,
                "sorting": sorting,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def reset_all_sessions_of_auser(self, email: Annotated[Any, '(Required) Email ID of the user whose sessions you want to reset. Note that this user will be signed out from all devices.'] = None) -> Any:
        """
        Reset all active sessions for a specified user, requiring them to sign in again across all devices.
        
        Args:
            email: The email ID of the user whose sessions are to be reset (Annotated as required).
        
        Returns:
            JSON response from the server after resetting the sessions.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            reset, session-management, security, async, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "email": email,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_organization_info(self, ) -> Any:
        """
        Retrieves organization information from the Miro API, including details available only to Enterprise plan users with Company Admin role.
        
        Args:
            None: This function does not take additional parameters beyond the class instance.
        
        Returns:
            dict: Parsed JSON response containing organization details from the Miro API.
        
        Raises:
            requests.HTTPError: Raised when the API request fails, typically due to insufficient permissions (non-Admin users), invalid organization scope, or authentication errors. Also occurs for requests made by non-Enterprise plan users.
        
        Tags:
            retrieve, organizations, api, enterprise-only, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_organization_members(self, active: Annotated[Any, ''] = None, cursor: Annotated[Any, ''] = None, emails: Annotated[Any, ''] = None, license: Annotated[Any, ''] = None, limit: Annotated[Any, ''] = None, role: Annotated[Any, ''] = None) -> Any:
        """
        Retrieves organization members based on specified criteria like emails or cursor.
        
        Args:
            active: Optional parameter to filter by active status.
            cursor: Optional cursor for pagination.
            emails: Optional list of emails to filter members.
            license: Optional license status to filter members.
            limit: Optional limit on the number of members to return.
            role: Optional role to filter members.
        
        Returns:
            A JSON response containing the organization members matching the specified criteria.
        
        Raises:
            HTTPError: Raised if the HTTP request to retrieve members fails (e.g., due to network issues or invalid server responses).
        
        Tags:
            organization, members, fetch, enterprise, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "emails": emails,
                "role": role,
                "license": license,
                "active": active,
                "cursor": cursor,
                "limit": limit,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_organization_member(self, ) -> Any:
        """
        Retrieves organization member information from the Miro API with Company Admin permissions.
        
        Returns:
            Dict[str, Any]: JSON response containing organization member details
        
        Raises:
            requests.HTTPError: Raised for HTTP request failures (4xx/5xx status codes), indicating authentication errors, permissions issues, or API rate limits exceeded
        
        Tags:
            organization-members, management, enterprise, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_boards(self, limit: Annotated[Any, ''] = None, offset: Annotated[Any, ''] = None, owner: Annotated[Any, ''] = None, project_id: Annotated[Any, ''] = None, query: Annotated[Any, ''] = None, sort: Annotated[Any, ''] = None, team_id: Annotated[Any, ''] = None) -> Any:
        """
        Retrieves a list of boards accessible to the user, allowing filtering by team, project, and other parameters.
        
        Args:
            limit: Limits the number of returned boards (pagination).
            offset: Offset for paginated results.
            owner: Filters results by owner ID.
            project_id: Filters boards by associated project ID.
            query: Free-text search query for board titles/descriptions.
            sort: Sorting criteria for results (field:direction format).
            team_id: Filters boards by associated team ID.
        
        Returns:
            Parsed JSON response containing board data and metadata.
        
        Raises:
            HTTPError: Raised for unsuccessful API responses (4XX/5XX status codes).
        
        Tags:
            boards, list, filter, pagination, async_job, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "team_id": team_id,
                "project_id": project_id,
                "query": query,
                "owner": owner,
                "limit": limit,
                "offset": offset,
                "sort": sort,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def copy_board(self, copy_from: Annotated[Any, '(Required) Unique identifier (ID) of the board that you want to copy.'] = None, description: Annotated[Any, ''] = None, name: Annotated[Any, ''] = None, policy: Annotated[dict[str, Any], ''] = None, teamId: Annotated[Any, ''] = None) -> Any:
        """
        Creates a copy of an existing board, allowing updates to name, description, sharing policy, and permissions policy.
        
        Args:
            copy_from: Unique identifier (ID) of the board to copy.
            description: Optional description for the new board.
            name: Optional name for the new board.
            policy: Optional policy settings for the new board.
            teamId: Optional team ID for the new board.
        
        Returns:
            The response from creating the new board, represented as JSON.
        
        Raises:
            HTTPError: Raised if the HTTP request fails.
        
        Tags:
            copy, board, management, important
        """
        request_body = {
            "description": description,
            "name": name,
            "policy": policy,
            "teamId": teamId,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "copy_from": copy_from,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_board(self, description: Annotated[Any, ''] = None, name: Annotated[Any, ''] = None, policy: Annotated[dict[str, Any], ''] = None, projectId: Annotated[Any, ''] = None, teamId: Annotated[Any, ''] = None) -> Any:
        """
        Creates a new board with specified attributes and sharing policies.
        
        Args:
            description: Optional description of the board.
            name: Name of the board to create.
            policy: Dictionary containing sharing policies for the board.
            projectId: ID of the associated project.
            teamId: ID of the team owning the board.
        
        Returns:
            Dictionary containing the created board details from API response.
        
        Raises:
            HTTPError: If API request fails due to invalid parameters, permissions, or rate limits.
        
        Tags:
            boards, create, management, async_job, important
        """
        request_body = {
            "description": description,
            "name": name,
            "policy": policy,
            "projectId": projectId,
            "teamId": teamId,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_specific_board(self, ) -> Any:
        """
        Retrieves information about a specific board from the Miro API.
        
        Args:
            None: This function does not take parameters.
        
        Returns:
            A JSON object containing board data returned by the API.
        
        Raises:
            requests.HTTPError: Raised when the API request fails, typically due to invalid permissions, missing board, or rate limits.
        
        Tags:
            retrieve, board, api, boards-read, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_board(self, ) -> Any:
        """
        Deletes a board, moving it to the trash where it can be restored within 90 days.
        
        Returns:
            The JSON response from the deletion request
        
        Raises:
            HTTPError: Raised if there is an issue with the HTTP request, such as a non-200 status code.
        
        Tags:
            delete, board, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_board(self, description: Annotated[Any, ''] = None, name: Annotated[Any, ''] = None, policy: Annotated[dict[str, Any], ''] = None, projectId: Annotated[Any, ''] = None, teamId: Annotated[Any, ''] = None) -> Any:
        """
        Updates a specific board by modifying its description, name, policy, project ID, or team ID.
        
        Args:
            description: The new description for the board.
            name: The new name for the board.
            policy: The new policy for the board, represented as a dictionary.
            projectId: The ID of the project to which the board belongs.
            teamId: The ID of the team associated with the board.
        
        Returns:
            The updated board data in JSON format.
        
        Raises:
            HTTPError: Raised if the HTTP request fails or if the API endpoint returns an error status code.
        
        Tags:
            update, boards, management, important
        """
        request_body = {
            "description": description,
            "name": name,
            "policy": policy,
            "projectId": projectId,
            "teamId": teamId,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_app_card_item(self, data: Annotated[dict[str, Any], ''] = None, geometry: Annotated[dict[str, Any], ''] = None, parent: Annotated[dict[str, Any], ''] = None, position: Annotated[dict[str, Any], ''] = None, style: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Creates an app card item and adds it to a Miro board, constructing the request from provided parameters.
        
        Args:
            data: Dictionary containing app card content and metadata (e.g., custom fields)
            geometry: Dictionary specifying dimensions and shape of the app card
            parent: Dictionary identifying the parent element/container for the app card
            position: Dictionary defining positioning coordinates (x/y axis) on the board
            style: Dictionary containing styling attributes like color and border
        
        Returns:
            Parsed JSON response containing created app card details
        
        Raises:
            HTTPError: On API request failure (4xx/5xx status codes)
        
        Tags:
            app-cards, create, board-items, async-jobs, management, important
        """
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_app_card_item(self, ) -> Any:
        """
        Retrieves information for a specific app card item on a Miro board.
        
        Returns:
            Dictionary containing the app card item data, or None if unavailable (depends on API response structure)
        
        Raises:
            requests.HTTPError: Raised for HTTP request failures (4XX client errors or 5XX server errors)
        
        Tags:
            app-cards, retrieve, api-client, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_app_card_item(self, ) -> Any:
        """
        Deletes an app card item from a board, requiring the boards:write scope and subject to rate limiting at Level 3.
        
        Args:
            None: This function does not take any arguments.
        
        Returns:
            The JSON response from the server after deletion.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returned an unsuccessful status code.
        
        Tags:
            delete, app-cards, boards-management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_app_card_item(self, data: Annotated[dict[str, Any], ''] = None, geometry: Annotated[dict[str, Any], ''] = None, parent: Annotated[dict[str, Any], ''] = None, position: Annotated[dict[str, Any], ''] = None, style: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Updates an app card item's properties including data, geometry, parent relationship, position, and style on a Miro board.
        
        Args:
            data: Dictionary containing app card data properties to update
            geometry: Dictionary specifying geometric properties like dimensions
            parent: Dictionary defining parent item relationships
            position: Dictionary containing positioning information
            style: Dictionary describing visual style attributes
        
        Returns:
            Dictionary containing the updated app card item's data from the API response
        
        Raises:
            HTTPError: When the API request fails (e.g., invalid parameters, authentication errors, or server issues)
        
        Tags:
            app-cards, update, board-items, important, management
        """
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_card_item(self, data: Annotated[dict[str, Any], ''] = None, geometry: Annotated[dict[str, Any], ''] = None, parent: Annotated[dict[str, Any], ''] = None, position: Annotated[dict[str, Any], ''] = None, style: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Creates a new card item and adds it to a Miro board with specified properties.
        
        Args:
            data: Dictionary containing card-specific data (content/metadata) [1]
            geometry: Dictionary defining card dimensions and shape characteristics [1]
            parent: Dictionary specifying parent item/container for the card [1]
            position: Dictionary containing coordinates for card placement [1]
            style: Dictionary containing visual styling properties for the card [1]
        
        Returns:
            Dictionary representing created card item from Miro API response after successful creation [1]
        
        Raises:
            HTTPError: Raised for unsuccessful HTTP requests (4XX/5XX status codes) during API communication [1]
            ValueError: Raised if required parameters are missing or invalid based on Miro API requirements [1]
        
        Tags:
            create, card, board, miro, api-integration, important, async_job
        """
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_card_item(self, ) -> Any:
        """
        Retrieves information for a specific card item on a board
        
        Args:
            None: This function does not take any parameters.
        
        Returns:
            The JSON response containing card item information
        
        Raises:
            requests.RequestException: Raised if there is a problem with the HTTP request (e.g., network issues or invalid URL).
            ValueError: Raised if the response status indicates an error.
        
        Tags:
            important, card, boards, read, information
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_card_item(self, ) -> Any:
        """
        Deletes a card item from the Miro board.
        
        Args:
            None: This function does not take any explicit parameters.
        
        Returns:
            JSON response from the server after deletion.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            delete, card, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_card_item(self, data: Annotated[dict[str, Any], ''] = None, geometry: Annotated[dict[str, Any], ''] = None, parent: Annotated[dict[str, Any], ''] = None, position: Annotated[dict[str, Any], ''] = None, style: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Updates a card item on a board based on the provided data and style properties.
        
        Args:
            data: A dictionary containing data properties for the card item.
            geometry: A dictionary defining the geometry of the card item.
            parent: A dictionary specifying the parent item or container.
            position: A dictionary describing the position of the card item.
            style: A dictionary containing style properties for the card item.
        
        Returns:
            The updated card item data as JSON.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            update, card, management, async_job, important
        """
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_connectors(self, cursor: Annotated[Any, ''] = None, limit: Annotated[Any, ''] = None) -> Any:
        """
        Retrieves a list of connectors for a specific board using a cursor-based approach.
        
        Args:
            cursor: Cursor value for pagination, used to retrieve the next portion of results.
            limit: Maximum number of connectors to return in the response.
        
        Returns:
            A JSON response containing the list of connectors and a cursor for pagination.
        
        Raises:
            requests.HTTPError: Raised when the HTTP request returns an unsuccessful status code.
        
        Tags:
            connectors, board, pagination, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "cursor": cursor,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_connector(self, captions: Annotated[list[Any], ''] = None, endItem: Annotated[dict[str, Any], ''] = None, shape: Annotated[Any, ''] = None, startItem: Annotated[dict[str, Any], ''] = None, style: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Creates a connector on a board by sending a POST request with specified parameters.
        
        Args:
            captions: List of captions for the connector.
            endItem: Dictionary representing the end item of the connector.
            shape: Shape of the connector.
            startItem: Dictionary representing the start item of the connector.
            style: Dictionary defining the style of the connector.
        
        Returns:
            JSON response from the server after creating the connector.
        
        Raises:
            requests.HTTPError: Raised when the HTTP request encounters an error.
        
        Tags:
            create, connector, important, boards, management
        """
        request_body = {
            "captions": captions,
            "endItem": endItem,
            "shape": shape,
            "startItem": startItem,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_specific_connector(self, ) -> Any:
        """
        Retrieves information for a specific connector on a board.
        
        Args:
            None: This function does not accept any arguments.
        
        Returns:
            A JSON response containing the information about the specific connector.
        
        Raises:
            requests.exceptions.HTTPError: Raised if there is an issue with the HTTP request, such as a failed status code.
        
        Tags:
            retrieve, connectors, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_connector(self, ) -> Any:
        """
        Error generating docstring: 1 validation error for DocstringOutput
        args
          Input should be a valid dictionary [type=dict_type, input_value='None', input_type=str]
            For further information visit https://errors.pydantic.dev/2.11/v/dict_type
        
        Args:
            None: This function takes no arguments
        
        Tags:
            generation-error
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_connector(self, captions: Annotated[list[Any], ''] = None, endItem: Annotated[dict[str, Any], ''] = None, shape: Annotated[Any, ''] = None, startItem: Annotated[dict[str, Any], ''] = None, style: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Updates a connector's properties on a board including captions, end/start items, shape, and style. Applies provided changes and returns updated connector data.
        
        Args:
            captions: List of captions to update on the connector (None preserves existing values)
            endItem: Dictionary defining the end item properties (None preserves existing values)
            shape: Updated connector shape specification (None preserves existing value)
            startItem: Dictionary defining the start item properties (None preserves existing values)
            style: Dictionary containing style properties to update (None preserves existing values)
        
        Returns:
            Dictionary containing the updated connector data from the API response
        
        Raises:
            requests.HTTPError: Raised for invalid requests (4XX client errors) or server failures (5XX errors)
        
        Tags:
            connector, update, board, miro, api-integration, management, important
        """
        request_body = {
            "captions": captions,
            "endItem": endItem,
            "shape": shape,
            "startItem": startItem,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_document_item_using_url(self, data: Annotated[dict[str, Any], ''] = None, geometry: Annotated[dict[str, Any], ''] = None, parent: Annotated[dict[str, Any], ''] = None, position: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Create a document item on a board using a URL, adding it with specified data, geometry, position, and parent relationships.
        
        Args:
            data: Dictionary containing document URL and metadata (Annotated as dict[str, Any])
            geometry: Dictionary defining dimensions and visual properties of the item (Annotated as dict[str, Any])
            parent: Dictionary specifying parent item relationships (Annotated as dict[str, Any])
            position: Dictionary containing positional coordinates (x/y) for board placement (Annotated as dict[str, Any])
        
        Returns:
            Dictionary containing the created document item's details from the API response
        
        Raises:
            requests.HTTPError: Raised for unsuccessful API responses (4XX/5XX status codes)
        
        Tags:
            create, document, async_job, management, important
        """
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_document_item(self, ) -> Any:
        """
        Retrieves information for a specific document item from a Miro board.
        
        Returns:
            Parsed JSON response containing the document item details.
        
        Raises:
            requests.HTTPError: If the HTTP request fails, such as due to invalid board ID, missing permissions, or rate-limiting.
        
        Tags:
            get, document, board, rest-api, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_document_item(self, ) -> Any:
        """
        Deletes a document item from the board, requiring a specific scope and rate limit tier.
        
        Returns:
            Parsed JSON response containing the result of the deletion operation
        
        Raises:
            HTTPError: Raised for unsuccessful HTTP responses (status codes >= 400), such as invalid permissions, missing document, or rate limit violations
        
        Tags:
            delete, management, documents, board, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_document_item_using_url(self, data: Annotated[dict[str, Any], ''] = None, geometry: Annotated[dict[str, Any], ''] = None, parent: Annotated[dict[str, Any], ''] = None, position: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Updates a document item using a URL by sending a PATCH request with the provided data, geometry, parent, and position.
        
        Args:
            data: Dictionary containing data to update. Default is None.
            geometry: Dictionary containing geometry to update. Default is None.
            parent: Dictionary containing parent information to update. Default is None.
            position: Dictionary containing position to update. Default is None.
        
        Returns:
            Returns the response from the API as JSON.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            update, document, patch, api-call, important
        """
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_document_item_using_file_from_device(self, request_body: Annotated[Any, ''] = None) -> Any:
        """
        Creates a document item on a board by uploading a file from the user's device.
        
        Args:
            request_body: Data containing file details and board specifications (format not explicitly documented)
        
        Returns:
            Dictionary containing created document item data from API response
        
        Raises:
            HTTPError: If API request fails due to invalid scope, rate limiting, or server error
        
        Tags:
            create, document, file-upload, async_job, management, important
        """
        request_body = request_body
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_document_item_using_file_from_device(self, request_body: Annotated[Any, ''] = None) -> Any:
        """
        Updates a document item on a Miro board using a file from a connected device. Requires boards:write scope.
        
        Args:
            request_body: Annotated dictionary containing file data and board/document identifiers for the update operation (type and structure determined by Miro API requirements).
        
        Returns:
            Dict containing updated document metadata from Miro API response
        
        Raises:
            HTTPError: On API request failure (4xx/5xx status codes), including invalid permissions, missing items, or rate limits
        
        Tags:
            update, document, file-upload, async_job, management, boards:write, important
        """
        request_body = request_body
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_embed_item(self, data: Annotated[dict[str, Any], ''] = None, geometry: Annotated[dict[str, Any], ''] = None, parent: Annotated[dict[str, Any], ''] = None, position: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Creates an embed item to add external content to a Miro board. Requires boards:write scope and adheres to Level 2 rate limiting.
        
        Args:
            data: Dictionary containing embed item data. Represents the external content's configuration.
            geometry: Dictionary specifying dimensions (width/height) and optional transformations for the embed item.
            parent: Dictionary identifying the parent element (e.g., frame) to which this embed item belongs. Optional.
            position: Dictionary specifying placement coordinates (x/y) for the embed item on the board.
        
        Returns:
            Dictionary containing the created embed item's details and metadata from the API response.
        
        Raises:
            HTTPError: Raised if the API request fails (4xx/5xx status codes). Includes error details from the response.
        
        Tags:
            create, embed, miro, api-integration, important
        """
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_embed_item(self, ) -> Any:
        """
        Retrieves information for a specific embed item on a board.
        
        Args:
            None: This function does not take any arguments.
        
        Returns:
            The embed item information in JSON format.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            embeds, read, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_embed_item(self, ) -> Any:
        """
        Delete an embed item from a board.
        
        Returns:
            JSON response containing deletion confirmation or data from the API.
        
        Raises:
            requests.exceptions.HTTPError: If the API request fails due to client or server errors (4XX/5XX responses).
        
        Tags:
            delete, embeds, management, api, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_embed_item(self, data: Annotated[dict[str, Any], ''] = None, geometry: Annotated[dict[str, Any], ''] = None, parent: Annotated[dict[str, Any], ''] = None, position: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Updates an embed item on a Miro board with specified properties, including data, geometry, parent relationships, and positioning.
        
        Args:
            data: Dictionary containing data properties to update for the embed item (e.g., metadata, content).
            geometry: Dictionary defining the embed item's dimensions and shape (e.g., height, width).
            parent: Dictionary specifying parent item relationships or containment details.
            position: Dictionary containing positioning information (e.g., x/y coordinates, rotation).
        
        Returns:
            Dictionary containing the updated embed item details from the Miro API response.
        
        Raises:
            HTTPError: Raised for unsuccessful API responses (4xx/5xx status codes) after calling self._patch().
        
        Tags:
            update, embed, board, management, api, patch, important
        """
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_image_item_using_url(self, data: Annotated[dict[str, Any], ''] = None, geometry: Annotated[dict[str, Any], ''] = None, parent: Annotated[dict[str, Any], ''] = None, position: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Creates an image item on a Miro board using a URL, adding the image to the board with specified data and positioning.
        
        Args:
            data: Dictionary containing image data (e.g., URL and metadata)
            geometry: Dictionary defining the image dimensions and geometric properties
            parent: Dictionary specifying the parent item or container for the image
            position: Dictionary detailing the image's placement coordinates on the board
        
        Returns:
            Parsed JSON response containing the created image item details
        
        Raises:
            HTTPError: Raised for unsuccessful API requests (e.g., invalid scope, rate limiting, or malformed data)
        
        Tags:
            images, create, miro-api, board-management, important
        """
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_image_item(self, ) -> Any:
        """
        Retrieves information for a specific image item on a board.
        
        Returns:
            JSON data containing image item information.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            images, read, board, fetch, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_image_item(self, ) -> Any:
        """
        Deletes an image item from the board.
        
        Args:
            None: This function does not accept any arguments.
        
        Returns:
            JSON response from the server after deleting the image item.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            delete, image-management, boards, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_image_item_using_url(self, data: Annotated[dict[str, Any], ''] = None, geometry: Annotated[dict[str, Any], ''] = None, parent: Annotated[dict[str, Any], ''] = None, position: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Updates an image item on a Miro board using URL, modifying its data, geometry, parent, or position.
        
        Args:
            data: Optional dictionary containing image data. Must comply with Miro's API requirements for image items.
            geometry: Optional dictionary specifying image dimensions (width/height) and optional transformations.
            parent: Optional dictionary identifying the parent element where the image should be placed.
            position: Optional dictionary containing coordinates (x/y) for image placement on the board.
        
        Returns:
            Dictionary containing the updated image item data from the Miro API response.
        
        Raises:
            requests.HTTPError: Raised for HTTP request failures, including invalid parameters (400), authentication errors (401), or resource not found (404).
        
        Tags:
            image, update, miro, async_job, important
        """
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_image_item_using_file_from_device(self, request_body: Annotated[Any, ''] = None) -> Any:
        """
        Creates an image item in a board by uploading a file from the device.
        
        Args:
            request_body: Optional body of the request, annotated with any data type. Defaults to None.
        
        Returns:
            The JSON response from the server after successfully creating the image item.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            image, upload, management, important
        """
        request_body = request_body
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_image_item_using_file_from_device(self, request_body: Annotated[Any, ''] = None) -> Any:
        """
        Updates an image item on a Miro board using a file from the user's device
        
        Args:
            request_body: Payload containing image data and configuration (type and structure determined by Miro API specifications)
        
        Returns:
            Parsed JSON representation of the updated image item from Miro API response
        
        Raises:
            HTTPError: On unsuccessful API request status codes (4xx/5xx responses)
        
        Tags:
            update, images, management, api-client, important
        """
        request_body = request_body
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_items_on_board(self, cursor: Annotated[Any, ''] = None, limit: Annotated[Any, ''] = None, type: Annotated[Any, ''] = None) -> Any:
        """
        Retrieves items from a specific board using cursor-based pagination.
        
        Args:
            cursor: Optional cursor value for retrieving the next portion of results.
            limit: Optional limit for the number of items to retrieve.
            type: Optional type of items to filter by.
        
        Returns:
            A JSON response containing the list of items on the board.
        
        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request.
        
        Tags:
            retrieve, pagination, board, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "type": type,
                "cursor": cursor,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_specific_item_on_board(self, ) -> Any:
        """
        Retrieves information for a specific item on a board.
        
        Args:
            None: This function takes no parameters.
        
        Returns:
            A JSON object containing information about the specific item.
        
        Raises:
            requests.HTTPError: This exception is raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            item, board, read, important, management
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_item(self, ) -> Any:
        """
        Deletes an item from a board, requiring specific permissions and adhering to rate limiting policies.
        
        Returns:
            dict: Parsed JSON response containing deletion confirmation details
        
        Raises:
            HTTPError: If the API request fails due to invalid permissions, missing resources, or exceeding rate limits
        
        Tags:
            delete, items, async_job, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_item_position_or_parent(self, parent: Annotated[dict[str, Any], ''] = None, position: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Updates the position or the parent of an item on a board.
        
        Args:
            parent: Optional parent dictionary to update the item's parent.
            position: Optional position dictionary to update the item's position.
        
        Returns:
            JSON response from the server containing the updated item details.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request fails due to invalid status code.
        
        Tags:
            update, management, board, item, important
        """
        request_body = {
            "parent": parent,
            "position": position,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_items_within_frame(self, cursor: Annotated[Any, ''] = None, limit: Annotated[Any, ''] = None, parent_item_id: Annotated[Any, '(Required) ID of the frame for which you want to retrieve the list of available items.'] = None, type: Annotated[Any, ''] = None) -> Any:
        """
        Retrieves a list of items within a specific frame using a cursor-based approach.
        
        Args:
            cursor: Cursor to retrieve the next portion of the results, if applicable.
            limit: Maximum number of items to return in the response.
            parent_item_id: Required ID of the frame from which to retrieve items.
            type: Type of items to retrieve.
        
        Returns:
            A JSON response containing items within the frame and potentially a cursor for pagination.
        
        Raises:
            HTTPError: Raised if the HTTP request to retrieve items fails.
        
        Tags:
            fetch, pagination, items, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "parent_item_id": parent_item_id,
                "limit": limit,
                "type": type,
                "cursor": cursor,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_specific_item_on_board1(self, ) -> Any:
        """
        Retrieves information for a specific item on a board from the Miro API, requiring read access to board data.
        
        Args:
            None: This method does not take parameters directly. Operates through class instance attributes (implied).
        
        Returns:
            Any: Parsed JSON response containing the board item's details.
        
        Raises:
            HTTPError: When the API request fails due to authentication issues, invalid parameters, or server errors (raised by response.raise_for_status()).
        
        Tags:
            retrieve, board-item, miro-api, async_job, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_item1(self, ) -> Any:
        """
        Deletes an item from the board.
        
        Args:
            None: No arguments are required.
        
        Returns:
            A JSON response from the server after deleting the item.
        
        Raises:
            requests.RequestException: Raised if there is an error with the request, such as network issues.
        
        Tags:
            delete, item_management, board, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_board_members(self, limit: Annotated[Any, ''] = None, offset: Annotated[Any, ''] = None) -> Any:
        """
        Retrieves a pageable list of all members for a board with optional pagination using limit and offset parameters.
        
        Args:
            limit: Optional limit on the number of members returned.
            offset: Optional offset for pagination, determining where the list begins.
        
        Returns:
            A JSON response containing the list of board members.
        
        Raises:
            HTTPError: Raised if the HTTP request fails, such as exceeding rate limits or unauthorized access.
        
        Tags:
            list, pagination, board, members, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def share_board(self, emails: Annotated[list[Any], ''] = None, message: Annotated[Any, ''] = None, role: Annotated[Any, ''] = None) -> Any:
        """
        Shares a board and invites new members by sending an invitation email based on provided parameters.
        
        Args:
            emails: A list of email addresses for the users to whom the board will be shared.
            message: An optional message to include in the invitation email.
            role: The role assigned to the invited users.
        
        Returns:
            A JSON response containing the result of the sharing operation.
        
        Raises:
            requests.HTTPError: Raised if there is a problem with the HTTP request, such as unauthorized access or a rate limit exceeded.
        
        Tags:
            share, invite, management, important
        """
        request_body = {
            "emails": emails,
            "message": message,
            "role": role,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_specific_board_member(self, ) -> Any:
        """
        Retrieves information for a specific board member.
        
        Args:
            None: This function does not accept additional parameters beyond the class instance
        
        Returns:
            A JSON response containing details about the board member.
        
        Raises:
            HTTPError: Raised if the HTTP request to retrieve the board member information fails, often due to an invalid response status.
        
        Tags:
            read, board-members, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_board_member(self, ) -> Any:
        """
        Removes a board member from a board.
        
        Args:
            None: This function does not take any parameters.
        
        Returns:
            The JSON response from the API after removing the board member.
        
        Raises:
            requests.HTTPError: If the HTTP request fails, such as encountering an unexpected status code.
        
        Tags:
            remove, board-members, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_board_member(self, role: Annotated[Any, ''] = None) -> Any:
        """
        Updates the role of a specific board member by submitting a PATCH request with the new role.
        
        Args:
            role: New role to assign to the board member. Required scope: boards:write.
        
        Returns:
            JSON response from the API containing updated board member data.
        
        Raises:
            requests.HTTPError: Raised if the API request fails (e.g., invalid role, insufficient permissions, or rate limiting).
        
        Tags:
            update, board-members, management, api, patch, important
        """
        request_body = {
            "role": role,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_shape_item(self, data: Annotated[dict[str, Any], ''] = None, geometry: Annotated[dict[str, Any], ''] = None, parent: Annotated[dict[str, Any], ''] = None, position: Annotated[dict[str, Any], ''] = None, style: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Creates a shape item on a board with specified properties and optional components.
        
        Args:
            data: Additional data associated with the shape (e.g., custom metadata).
            geometry: Geometric properties of the shape (e.g., dimensions, type).
            parent: Parent element or container for the shape (e.g., group, frame).
            position: Positioning information (e.g., x/y coordinates, rotation).
            style: Styling attributes (e.g., color, border thickness, fill).
        
        Returns:
            JSON response containing details of the created shape item.
        
        Raises:
            HTTPError: If the API request fails due to invalid parameters, authentication issues, or server errors.
        
        Tags:
            shapes, board-management, api, create, important
        """
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_shape_item(self, ) -> Any:
        """
        Retrieve information for a specific shape item on a board.
        
        Args:
            None: This function takes no parameters.
        
        Returns:
            A JSON object containing the shape item's information.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            retrieve, board, item, shape, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_shape_item(self, ) -> Any:
        """
        Deletes a shape item from the board. Requires Miro API authorization with 'boards:write' scope and adheres to Level 3 rate limiting.
        
        Args:
            None: This instance method does not require additional parameters beyond the class instance itself.
        
        Returns:
            Dict[str, Any]: Parsed JSON response containing API operation results.
        
        Raises:
            RequestException: If the HTTP request fails due to connection errors or invalid parameters.
            HTTPError: If the API responds with a status code indicating failure (e.g., 404 for invalid resource or 403 for insufficient permissions).
        
        Tags:
            delete, shapes, board, management, api, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_shape_item(self, data: Annotated[dict[str, Any], ''] = None, geometry: Annotated[dict[str, Any], ''] = None, parent: Annotated[dict[str, Any], ''] = None, position: Annotated[dict[str, Any], ''] = None, style: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Updates a shape item on a board based on the provided data, geometry, parent, position, and style.
        
        Args:
            data: Dictionary containing the data for the shape item.
            geometry: Dictionary defining the geometry of the shape item.
            parent: Dictionary specifying the parent of the shape item.
            position: Dictionary with the position details of the shape item.
            style: Dictionary containing the styling properties for the shape item.
        
        Returns:
            JSON response from the update operation.
        
        Raises:
            HTTPError: Raised if the HTTP request fails.
        
        Tags:
            update, shape, management, important
        """
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_sticky_note_item(self, data: Annotated[dict[str, Any], ''] = None, geometry: Annotated[dict[str, Any], ''] = None, parent: Annotated[dict[str, Any], ''] = None, position: Annotated[dict[str, Any], ''] = None, style: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Creates a sticky note item on a Miro board with specified properties.
        
        Args:
            data: Dictionary containing sticky note content/metadata. See Miro API documentation for required fields.
            geometry: Dictionary defining dimensions (e.g., width/height) of the sticky note.
            parent: Dictionary identifying parent element when nesting sticky notes.
            position: Dictionary specifying x/y coordinates for sticky note placement.
            style: Dictionary containing styling attributes (e.g., color, text formatting).
        
        Returns:
            Dictionary containing created sticky note details from Miro API response
        
        Raises:
            HTTPError: Raised for API request failures (4XX/5XX status codes)
        
        Tags:
            create, sticky-notes, api-integration, board-management, important
        """
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_sticky_note_item(self, ) -> Any:
        """
        Retrieves information for a specific sticky note item on a Miro board.
        
        Args:
            None: This function does not require parameters.
        
        Returns:
            Any: Parsed JSON response containing the sticky note item data.
        
        Raises:
            requests.HTTPError: Raised for HTTP request failures, such as invalid board access or API rate limits exceeded.
        
        Tags:
            sticky-note, retrieve, api-call, boards-read, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_sticky_note_item(self, ) -> Any:
        """
        Deletes a sticky note item from the board.
        
        Args:
            None: This function takes no arguments
        
        Returns:
            The JSON response from the server after deletion.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the HTTP request returns an unsuccessful status code.
        
        Tags:
            delete, sticky_notes, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_sticky_note_item(self, data: Annotated[dict[str, Any], ''] = None, geometry: Annotated[dict[str, Any], ''] = None, parent: Annotated[dict[str, Any], ''] = None, position: Annotated[dict[str, Any], ''] = None, style: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Updates a sticky note item on a board based on provided data and style properties.
        
        Args:
            data: Dictionary containing data to update for the sticky note item.
            geometry: Dictionary specifying the geometry of the sticky note item.
            parent: Dictionary identifying the parent of the sticky note item.
            position: Dictionary containing position information for the sticky note item.
            style: Dictionary specifying styling options for the sticky note item.
        
        Returns:
            JSON response from the API after updating the sticky note item.
        
        Raises:
            requests.exceptions.HTTPError: If the HTTP request returns an unsuccessful status code.
        
        Tags:
            update, sticky-notes, board-management, important
        """
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_text_item(self, data: Annotated[dict[str, Any], ''] = None, geometry: Annotated[dict[str, Any], ''] = None, parent: Annotated[dict[str, Any], ''] = None, position: Annotated[dict[str, Any], ''] = None, style: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Creates a text item on a board by sending a POST request with the specified parameters.
        
        Args:
            data: Dictionary containing data for the text item.
            geometry: Dictionary specifying the geometry of the text item.
            parent: Dictionary identifying the parent of the text item.
            position: Dictionary detailing the position of the text item.
            style: Dictionary that defines the style of the text item.
        
        Returns:
            JSON response from the server after creating the text item.
        
        Raises:
            HTTPError: Raised if the HTTP request is unsuccessful due to rate limiting or invalid request.
        
        Tags:
            create, text, board, write, important
        """
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_text_item(self, ) -> Any:
        """
        Retrieves information for a specific text item on a Miro board, requiring boards:read scope and subject to rate limiting.
        
        Args:
            None: This method does not accept any parameters.
        
        Returns:
            dict: A dictionary containing the text item data from the Miro API response.
        
        Raises:
            HTTPError: Raised for unsuccessful HTTP responses (4XX/5XX status codes).
        
        Tags:
            text, retrieve, miro-api, boards-read, rate-limited, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_text_item(self, ) -> Any:
        """
        Deletes a text item from a board, requiring specific permissions and adhering to rate limiting rules.
        
        Returns:
            Response data from the API call parsed as JSON.
        
        Raises:
            HTTPError: If the request fails due to rate limiting, insufficient permissions, or invalid parameters.
        
        Tags:
            delete, text-management, board-api, async_job, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_text_item(self, data: Annotated[dict[str, Any], ''] = None, geometry: Annotated[dict[str, Any], ''] = None, parent: Annotated[dict[str, Any], ''] = None, position: Annotated[dict[str, Any], ''] = None, style: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Updates a text item on a board based on the provided data and style properties.
        
        Args:
            data: Dictionary containing data properties for the text item.
            geometry: Dictionary containing geometry properties for the text item.
            parent: Dictionary specifying the parent of the text item.
            position: Dictionary containing position properties for the text item.
            style: Dictionary defining style properties for the text item.
        
        Returns:
            JSON response from the API request.
        
        Raises:
            RequestException: Raised if there is a problem with the HTTP request.
        
        Tags:
            update, text, important, management
        """
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_items_in_bulk(self, items: Annotated[list[Any], ''] = None) -> Any:
        """
        Creates items in bulk by adding up to 20 items of the same or different types to a board in a single transactional operation
        
        Args:
            items: A list of items of any type, which can include shapes, cards, or sticky notes. Defaults to None if no items are provided
        
        Returns:
            The JSON response from the successful creation operation
        
        Raises:
            HTTPError: Raised if the HTTP request fails, such as a non-200 status code
        
        Tags:
            bulk, transactional, create, important, management
        """
        request_body = items
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_items_in_bulk_using_file_from_device(self, request_body: Annotated[Any, ''] = None) -> Any:
        """
        Create items in bulk using a file from a device. This function adds different types of items to a board, supporting up to 20 items per call. The operation is transactional; if any item fails to create, none will be created.
        
        Args:
            request_body: The JSON body containing the bulk data for the items to be created. Optional.
        
        Returns:
            JSON response from the bulk creation operation.
        
        Raises:
            requests.HTTPError: Raises an HTTP error if the request status code indicates a failure.
        
        Tags:
            create, bulk, api, file, important
        """
        request_body = request_body
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_frame(self, data: Annotated[dict[str, Any], ''] = None, geometry: Annotated[dict[str, Any], ''] = None, position: Annotated[dict[str, Any], ''] = None, style: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Creates a new frame on a board by sending the provided data, geometry, position, and style.
        
        Args:
            data: Optional dictionary containing data for the frame.
            geometry: Optional dictionary specifying the geometry of the frame.
            position: Optional dictionary defining the position of the frame.
            style: Optional dictionary describing the style of the frame.
        
        Returns:
            The JSON response from the server after creating the frame.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            frame, create, board, important, management
        """
        request_body = {
            "data": data,
            "geometry": geometry,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_frame(self, ) -> Any:
        """
        Retrieves information for a specific frame on a Miro board.
        
        Args:
            None: This method does not accept parameters (acts on the instance's configured board context).
        
        Returns:
            Any: Parsed JSON response containing frame data and metadata.
        
        Raises:
            HTTPError: Raised for failed API requests (4XX/5XX status codes), typically due to invalid permissions, missing frames, or network issues.
        
        Tags:
            frames, retrieve, api, boards:read, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_frame(self, ) -> Any:
        """
        Delete a frame from a Miro board. Requires boards:write scope and adheres to Rate Limit Level 3.
        
        Args:
            None: This method does not accept parameters beyond the instance reference.
        
        Returns:
            dict: Response payload from the Miro API after successful deletion.
        
        Raises:
            requests.exceptions.HTTPError: Raised for HTTP request failures, including invalid permissions (403), non-existent frame (404), or rate limiting (429).
        
        Tags:
            delete, frame, management, async_job, boards, miro, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_frame(self, data: Annotated[dict[str, Any], ''] = None, geometry: Annotated[dict[str, Any], ''] = None, position: Annotated[dict[str, Any], ''] = None, style: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Updates a frame on a board using the provided data, style, geometry, or position properties.
        
        Args:
            data: A dictionary containing data properties to update the frame.
            geometry: A dictionary containing geometry properties to update the frame.
            position: A dictionary containing position properties to update the frame.
            style: A dictionary containing style properties to update the frame.
        
        Returns:
            JSON response from the server after updating the frame.
        
        Raises:
            HTTPError: Raised if the server returns an HTTP error (e.g., unauthorized access).
        
        Tags:
            update, frames, important, management
        """
        request_body = {
            "data": data,
            "geometry": geometry,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_app_metrics(self, endDate: Annotated[Any, '(Required) End date of the period in UTC format. For example, 2024-12-31.'] = None, period: Annotated[Any, 'Group data by this time period.'] = None, startDate: Annotated[Any, '(Required) Start date of the period in UTC format. For example, 2024-12-31.'] = None) -> Any:
        """
        Fetches app metrics for a specified time range and groups data by given period.
        
        Args:
            endDate: (Required) End date of the period in UTC format (e.g., 2024-12-31).
            period: Time period to group data by (e.g., day, week).
            startDate: (Required) Start date of the period in UTC format (e.g., 2024-12-31).
        
        Returns:
            List of usage metrics for the app grouped by the specified time period.
        
        Raises:
            requests.HTTPError: Raised if the API request fails (e.g., invalid parameters, authentication failure, or rate limiting).
        
        Tags:
            app-metrics, data-fetch, usage-analytics, important, management
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "startDate": startDate,
                "endDate": endDate,
                "period": period,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_total_app_metrics(self, ) -> Any:
        """
        Get total usage metrics for a specific app since its creation.
        
        Args:
            None: This function takes no parameters.
        
        Returns:
            A JSON object containing total app usage metrics.
        
        Raises:
            requests.RequestException: Raised if there is an issue with the API request or response handling.
        
        Tags:
            metrics, reporting, app-management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_webhook_subscription(self, boardId: Annotated[Any, ''] = None, callbackUrl: Annotated[Any, ''] = None, status: Annotated[Any, ''] = None) -> Any:
        """
        Creates a webhook subscription to receive item-update notifications for a specified Miro board.
        
        Args:
            boardId: ID of the board to monitor for item updates
            callbackUrl: URL endpoint that will receive notifications
            status: Current status of the webhook subscription (active by default when created)
        
        Returns:
            Dictionary containing the created subscription details from the API response
        
        Raises:
            requests.HTTPError: If the API request fails with non-2xx status code
        
        Tags:
            webhooks, subscriptions, api-integration, notifications, management, important
        """
        request_body = {
            "boardId": boardId,
            "callbackUrl": callbackUrl,
            "status": status,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_webhook_subscription(self, callbackUrl: Annotated[Any, ''] = None, status: Annotated[Any, ''] = None) -> Any:
        """
        Updates the status or callback URL of an existing webhook subscription.
        
        Args:
            callbackUrl: New URL for receiving webhook events. None preserves existing value.
            status: Updated status for the subscription (e.g., 'enabled', 'disabled'). None preserves existing value.
        
        Returns:
            Dictionary containing the updated webhook subscription details.
        
        Raises:
            HTTPError: Raised for API request failures, including invalid parameters or authorization issues.
        
        Tags:
            webhook, update, subscription, management, api, important
        """
        request_body = {
            "callbackUrl": callbackUrl,
            "status": status,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_webhook_subscriptions(self, cursor: Annotated[Any, ''] = None, limit: Annotated[Any, ''] = None) -> Any:
        """
        Retrieves information about webhook subscriptions for a user.
        
        Args:
            cursor: Optional cursor to specify where to start retrieving subscriptions
            limit: Optional limit on the number of subscriptions to return
        
        Returns:
            A JSON object containing information about the webhook subscriptions.
        
        Raises:
            HTTPError: Raised when the HTTP request to retrieve subscriptions fails.
        
        Tags:
            webhooks, list, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "cursor": cursor,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_specific_webhook_subscription(self, ) -> Any:
        """
        Retrieves information for a specific webhook subscription from the Miro API.
        
        Args:
            None: This function does not accept parameters directly. The subscription ID should be included in the base URL path.
        
        Returns:
            dict: Parsed JSON response containing the webhook subscription details.
        
        Raises:
            requests.exceptions.HTTPError: Raised for HTTP 4XX/5XX errors from the API request.
        
        Tags:
            webhooks, experimental, retrieve, api-call, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_webhook_subscription(self, ) -> Any:
        """
        Deletes the specified webhook subscription. Requires appropriate permissions and adherence to rate limiting.
        
        Args:
            None: This function does not accept parameters
        
        Returns:
            dict: Parsed JSON response containing the deletion confirmation or related data
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request fails (4XX/5XX status codes), typically due to invalid permissions, nonexistent subscription, or API rate limits being exceeded
        
        Tags:
            delete, webhook, subscription, api, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_specific_mind_map_node(self, ) -> Any:
        """
        Retrieves information for a specific mind map node on a Miro board, requiring boards:read scope.
        
        Returns:
            JSON-formatted response containing the mind map node's data.
        
        Raises:
            requests.HTTPError: Raised when the API request fails, typically due to invalid board access, missing nodes, or server errors.
        
        Tags:
            retrieve, mind-map-node, experimental, boards:read, api-call, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_mind_map_node(self, ) -> Any:
        """
        Error generating docstring: 1 validation error for DocstringOutput
        args
          Input should be a valid dictionary [type=dict_type, input_value='None', input_type=str]
            For further information visit https://errors.pydantic.dev/2.11/v/dict_type
        
        Args:
            None: This function takes no arguments
        
        Tags:
            generation-error
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_mind_map_nodes(self, cursor: Annotated[Any, 'Points to the next portion of the results set'] = None, limit: Annotated[Any, 'Maximum number of results returned'] = None) -> Any:
        """
        Retrieve mind map nodes using cursor-based pagination for a specific board.
        
        Args:
            cursor: Points to the next portion of the results set for pagination. Subsequent calls should use the cursor value from the previous response to retrieve the next batch.
            limit: Maximum number of results to return in a single batch.
        
        Returns:
            JSON response containing the list of mind map nodes and pagination cursor.
        
        Raises:
            requests.HTTPError: Raised for invalid requests, such as authentication failures or rate limit breaches, based on the API response status.
        
        Tags:
            mind-map, pagination, cursor-based, retrieve, async_job, boards:read, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "cursor": cursor,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_mind_map_node(self, data: Annotated[dict[str, Any], ''] = None, geometry: Annotated[dict[str, Any], ''] = None, parent: Annotated[dict[str, Any], ''] = None, position: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Create a mind map node, adding it to a board as either a root node or a child node under another node.
        
        Args:
            data: Optional data associated with the node, provided as a dictionary.
            geometry: Optional geometry data for the node, provided as a dictionary.
            parent: Optional parent node, provided as a dictionary, indicating the node this node will be a child of.
            position: Optional position parameters for the node, provided as a dictionary with x and y coordinates.
        
        Returns:
            The JSON response from the API call after creating the node.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request to create the node fails.
        
        Tags:
            create, mind-map, node-management, important
        """
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_items_on_board1(self, cursor: Annotated[Any, ''] = None, limit: Annotated[Any, ''] = None, type: Annotated[Any, ''] = None) -> Any:
        """
        Retrieve paginated items from a specific board using cursor-based pagination, with optional filtering by item type.
        
        Args:
            cursor: Cursor for pagination. Set to the cursor value from the previous response to retrieve the next page of results.
            limit: Maximum number of items to return per request.
            type: Filter items by specific type (if provided).
        
        Returns:
            JSON response containing the paginated list of items from the board.
        
        Raises:
            HTTPError: Raised when the HTTP request fails, typically due to authentication errors, invalid parameters, or rate limiting.
        
        Tags:
            list, paginated, cursor, filter, board-items, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "type": type,
                "cursor": cursor,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_shape_item1(self, data: Annotated[dict[str, Any], ''] = None, geometry: Annotated[dict[str, Any], ''] = None, parent: Annotated[dict[str, Any], ''] = None, position: Annotated[dict[str, Any], ''] = None, style: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Creates a flowchart shape item on a Miro board using the provided parameters.
        
        Args:
            data: Dictionary containing shape item data. See Miro API documentation for structure.
            geometry: Dictionary specifying geometric properties of the shape (e.g., dimensions).
            parent: Dictionary referencing a parent element for hierarchical structures.
            position: Dictionary specifying x/y coordinates for shape placement.
            style: Dictionary containing styling parameters (colors, borders, etc).
        
        Returns:
            Dictionary containing the created shape item's data from the Miro API response.
        
        Raises:
            HTTPError: When the Miro API request fails (4xx/5xx status codes).
        
        Tags:
            create, flowchart, shapes, boards:write, important
        """
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_shape_item1(self, ) -> Any:
        """
        Retrieves information for a specific shape item on a board.
        
        Args:
            None: This function does not take any parameters.
        
        Returns:
            A JSON response containing information about the shape item.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            retrieve, board-item, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_shape_item1(self, ) -> Any:
        """
        Deletes a flowchart shape item from the board.
        
        Args:
            None: This function does not take any parameters.
        
        Returns:
            The JSON response from the delete operation.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request returned an unsuccessful status code.
        
        Tags:
            delete, flowchart, shape, item, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_shape_item1(self, data: Annotated[dict[str, Any], ''] = None, geometry: Annotated[dict[str, Any], ''] = None, parent: Annotated[dict[str, Any], ''] = None, position: Annotated[dict[str, Any], ''] = None, style: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Updates a flowchart shape item on a board based on the provided data and style properties.
        
        Args:
            data: Dictionary containing data properties for the shape item.
            geometry: Dictionary containing geometric properties for the shape item.
            parent: Dictionary specifying the parent of the shape item.
            position: Dictionary defining the position of the shape item.
            style: Dictionary setting the visual style of the shape item.
        
        Returns:
            The JSON response from the server after updating the shape item.
        
        Raises:
            requests.RequestException: Raised if there is an issue with the HTTP request.
        
        Tags:
            update, flowchart-shapes, management, important
        """
        request_body = {
            "data": data,
            "geometry": geometry,
            "parent": parent,
            "position": position,
            "style": style,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_all_groups_on_aboard(self, cursor: Annotated[Any, ''] = None, limit: Annotated[Any, 'The maximum number of items to return at one time, default is 10, maximum is 50.'] = None) -> Any:
        """
        Retrieves all groups on a board, using a cursor-based pagination approach.
        
        Args:
            cursor: A cursor to fetch the next portion of results; defaults to None.
            limit: The maximum number of items to return at one time; defaults to 10, with a maximum of 50.
        
        Returns:
            A JSON response containing groups and their items, along with a cursor for pagination.
        
        Raises:
            HTTPError: Raised if the HTTP request encounters an error, such as a non-200 status code.
        
        Tags:
            fetch, groups, cursor-pagination, important, management
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "cursor": cursor,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_group(self, data: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Creates a group of items on a Miro board using the provided data dictionary.
        
        Args:
            data: Dictionary containing item data to create a group (None results in empty group creation with default parameters)
        
        Returns:
            JSON response containing the created group details from Miro API
        
        Raises:
            HTTPError: When the API request fails due to invalid input, insufficient permissions, or server issues
        
        Tags:
            create, group, management, boards, write, async-job, important
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_items_of_agroup_by_id(self, cursor: Annotated[Any, ''] = None, group_item_id: Annotated[Any, '(Required) The ID of the group item to retrieve.'] = None, limit: Annotated[Any, 'The maximum number of items to return at one time, default is 10, maximum is 50.'] = None) -> Any:
        """
        Retrieves items of a group by ID using a cursor-based approach.
        
        Args:
            cursor: Cursor value for pagination. If None, returns the first set of results.
            group_item_id: The ID of the group item to retrieve. This parameter is required.
            limit: The maximum number of items to return at one time (default is 10, maximum is 50).
        
        Returns:
            A JSON response containing a list of items that are part of the specified group.
        
        Raises:
            requests.HTTPError: Raised if there was an HTTP error during the request.
        
        Tags:
            retrieve, group, cursor-based, async_job, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "cursor": cursor,
                "group_item_id": group_item_id,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_agroup_by_its_id(self, ) -> Any:
        """
        Failed to extract docstring information
        
        Args:
            None: This function takes no arguments
        
        Returns:
            Unknown return value
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def updates_agroup_with_new_items(self, data: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Updates an existing group entirely by replacing it with new data and assigns a new group ID.
        
        Args:
            data: A dictionary containing the new data to replace the group. It is optional and defaults to None.
        
        Returns:
            The JSON response from the server after updating the group.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returned an unsuccessful status code.
        
        Tags:
            update, group, management, important
        """
        request_body = {
            "data": data,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._put(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def ungroup_items(self, delete_items: Annotated[Any, 'Indicates whether the items should be removed. By default, false.'] = None) -> Any:
        """
        Ungroups items from a group, optionally deleting them.
        
        Args:
            delete_items: Indicates whether the items should be removed; defaults to None, meaning no deletion by default.
        
        Returns:
            A JSON response from the server.
        
        Raises:
            requests.exceptions.HTTPError: Raised if there is an HTTP error in the request, such as rate limiting or unauthorized access.
        
        Tags:
            ungroup, delete, groups, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "delete_items": delete_items,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def deletes_the_group(self, delete_items: Annotated[Any, '(Required) Indicates whether the items should be removed. Set to `true` to delete items in the group.'] = None) -> Any:
        """
        Deletes a group from the board, optionally removing items within it.
        
        Args:
            delete_items: Indicates whether the items should be removed. Set to `true` to delete items in the group.
        
        Returns:
            Response from deleting the group, represented as JSON.
        
        Raises:
            requests.HTTPError: Raised when an HTTP error occurs, such as an invalid response status.
        
        Tags:
            delete, group-management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "delete_items": delete_items,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def revoke_token_v2(self, accessToken: Annotated[Any, ''] = None, clientId: Annotated[Any, ''] = None, clientSecret: Annotated[Any, ''] = None) -> Any:
        """
        Revoke an access token and its associated refresh token, invalidating them immediately and preventing further use. This action does not uninstall the application for the user.
        
        Args:
            accessToken: Access token to revoke (required for token invalidation)
            clientId: Client ID associated with the OAuth application (required for authentication)
            clientSecret: Client secret associated with the OAuth application (required for authentication)
        
        Returns:
            Parsed JSON response from the revocation endpoint
        
        Raises:
            requests.HTTPError: Raised for non-2xx status codes from the API server, indicating authentication failures, invalid parameters, or server errors
        
        Tags:
            oauth, authentication, token-management, revoke, api, v2, important
        """
        request_body = {
            "accessToken": accessToken,
            "clientId": clientId,
            "clientSecret": clientSecret,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tags_from_item(self, ) -> Any:
        """
        Retrieves all tags associated with the specified item by making a GET request to the Miro API endpoint.
        
        Returns:
            A parsed JSON response containing tags associated with the item, typically as a list or dictionary structure.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the HTTP request fails due to invalid credentials, missing permissions (boards:read scope required), or invalid resource identifiers.
        
        Tags:
            get, retrieve, tags, api, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tags_from_board(self, limit: Annotated[Any, ''] = None, offset: Annotated[Any, ''] = None) -> Any:
        """
        Retrieves tags from a specified board using pagination parameters.
        
        Args:
            limit: Maximum number of tags to return (used for pagination).
            offset: Number of tags to skip before returning results (used for pagination).
        
        Returns:
            JSON response containing retrieved tags.
        
        Raises:
            HTTPError: If the API request fails due to client/server errors (4xx/5xx).
        
        Tags:
            retrieve, list, board, tags, pagination, rest-api, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "offset": offset,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_tag(self, fillColor: Annotated[Any, ''] = None, title: Annotated[Any, ''] = None) -> Any:
        """
        Creates a tag on a board with specified visual attributes, requiring API write access.
        
        Args:
            fillColor: (Any, optional): Hex code or color name for the tag's background fill.
            title: (Any, optional): Display text for the tag.
        
        Returns:
            Any: Parsed JSON response containing the created tag's metadata.
        
        Raises:
            HTTPError: If the API request fails due to invalid permissions, invalid parameters, rate limits, or server errors.
        
        Tags:
            management, board-tag, create, async-job, important
        """
        request_body = {
            "fillColor": fillColor,
            "title": title,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_tag(self, ) -> Any:
        """
        Retrieves information for a specific tag from the Miro API, requiring the 'boards:write' scope.
        
        Returns:
            Any: Parsed JSON response containing tag information from the Miro API
        
        Raises:
            HTTPError: If the API request fails due to authentication, invalid parameters, or server errors (forwarded from response.raise_for_status())
        
        Tags:
            retrieve, tag, boards-write, api-client, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_tag(self, ) -> Any:
        """
        Deletes a specified tag from the board, removing it from all cards and sticky notes.
        
        Args:
            None: This function takes no additional parameters.
        
        Returns:
            The response from the delete operation as JSON.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request encounters any error.
        
        Tags:
            delete, tag, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_tag(self, fillColor: Annotated[Any, ''] = None, title: Annotated[Any, ''] = None) -> Any:
        """
        Updates a tag's properties (fill color and title) on a Miro board. Changes made via API are not reflected in real-time until the board is refreshed.
        
        Args:
            fillColor: New fill color for the tag (optional)
            title: New title/text for the tag (optional)
        
        Returns:
            JSON response containing updated tag data from the Miro API
        
        Raises:
            requests.HTTPError: Raised for unsuccessful API responses (4xx/5xx status codes)
        
        Tags:
            update, tag, board, management, important
        """
        request_body = {
            "fillColor": fillColor,
            "title": title,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_items_by_tag(self, limit: Annotated[Any, ''] = None, offset: Annotated[Any, ''] = None, tag_id: Annotated[Any, '(Required) Unique identifier (ID) of the tag that you want to retrieve.'] = None) -> Any:
        """
        Retrieves items associated with a specified tag from a Miro board.
        
        Args:
            limit: Maximum number of items to retrieve (None returns all available items).
            offset: Starting position for paginated results.
            tag_id: Unique identifier (ID) of the tag to filter items (required).
        
        Returns:
            JSON response containing the retrieved items matching the specified tag.
        
        Raises:
            HTTPError: If the API request fails due to invalid scope, rate limiting, or invalid tag ID.
        
        Tags:
            retrieve, tag, items, pagination, api, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "offset": offset,
                "tag_id": tag_id,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def attach_tag_to_item(self, tag_id: Annotated[Any, '(Required) Unique identifier (ID) of the tag you want to add to the item.'] = None) -> Any:
        """
        Attaches an existing tag to a specified Miro board item (card or sticky note). Supports up to 8 tags per item.
        
        Args:
            tag_id: (Required) Unique identifier (ID) of the tag to attach to the item. Must be valid Miro tag ID.
        
        Returns:
            JSON response containing the API operation result. Format depends on Miro's API implementation.
        
        Raises:
            requests.exceptions.HTTPError: Raised for invalid tag IDs, non-existent items, rate limits (Level 1), or missing 'boards:write' scope permissions.
        
        Tags:
            tag-attachment, board-management, async_job, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "tag_id": tag_id,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._post(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_tag_from_item(self, tag_id: Annotated[Any, '(Required) Unique identifier (ID) of the tag that you want to remove from the item.'] = None) -> Any:
        """
        Removes a specific tag from an item without deleting the tag itself.
        
        Args:
            tag_id: Unique identifier (ID) of the tag to be removed from the item.
        
        Returns:
            The response of the deletion operation in JSON format.
        
        Raises:
            HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            remove, tag, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "tag_id": tag_id,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_of_projects(self, cursor: Annotated[Any, 'An indicator of the position of a page in the full set of results. To obtain the first page leave it empty. To obtain subsequent pages set it to the value returned in the cursor field of the previous request.'] = None, limit: Annotated[Any, 'The maximum number of results to return per call. If the number of projects in the response is greater than the limit specified, the response returns the cursor parameter with a value.'] = None) -> Any:
        """
        Retrieves a list of projects in an organization, including private projects with Content Admin permissions.
        
        Args:
            cursor: An indicator of the position of a page in the full set of results. To obtain the first page, leave it empty. To obtain subsequent pages, set it to the value returned in the cursor field of the previous request.
            limit: The maximum number of results to return per call.
        
        Returns:
            A JSON response containing the list of projects.
        
        Raises:
            HTTPError: Raised if an HTTP request error occurs, such as a bad response status code.
        
        Tags:
            list, projects, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "cursor": cursor,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_project(self, name: Annotated[Any, ''] = None) -> Any:
        """
        Creates a new project in an existing team as an organizational container for boards, enabling shared access management.
        
        Args:
            name: Name of the project (required). Projects act as folders for organizing boards with controlled access.
        
        Returns:
            Dictionary containing created project details from API response
        
        Raises:
            HTTPError: If the API request fails (e.g., invalid authentication, insufficient permissions, or missing required scope 'projects:write')
        
        Tags:
            projects, create, management, board-organization, async_job, enterprise, important
        """
        request_body = {
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_project(self, ) -> Any:
        """
        Retrieves project information, such as the name of an existing project.
        
        Args:
            None: This function takes no parameters.
        
        Returns:
            The project information in JSON format.
        
        Raises:
            HTTPError: Raised if the HTTP request encounters an error, such as a bad status code.
        
        Tags:
            management, project, enterprise, important, read
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_project(self, ) -> Any:
        """
        Deletes a project, retaining associated boards and users within the team.
        
        Args:
            None: This function takes no arguments.
        
        Returns:
            The JSON response from the server after deleting the project.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request returns an unsuccessful status code.
        
        Tags:
            delete, project, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_project(self, name: Annotated[Any, ''] = None) -> Any:
        """
        Updates project information, including the project name.
        
        Args:
            name: Project name to update (optional). Required scope: projects:write. Enterprise plan and Company Admin role required.
        
        Returns:
            JSON response containing updated project details.
        
        Raises:
            requests.HTTPError: Raised for failed API requests (4xx/5xx status codes).
            PermissionError: Implicitly raised if lacking Enterprise plan access or Company Admin privileges.
        
        Tags:
            update, project, management, enterprise, async_job, important
        """
        request_body = {
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_project_settings(self, ) -> Any:
        """
        Retrieves project settings from the Miro API. This endpoint requires specific permissions and is restricted to Enterprise plan users with Company Admin role.
        
        Returns:
            dict: A dictionary containing the project settings fetched from the Miro API
        
        Raises:
            requests.HTTPError: Raised when the API request fails, typically due to authentication issues or invalid permissions
        
        Tags:
            project-settings, management, enterprise, api-call, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_project_settings(self, sharingPolicySettings: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Updates the settings of a project, specifically modifying the sharing policy settings.
        
        Args:
            sharingPolicySettings: Optional dictionary containing settings for sharing policies; defaults to None if not provided.
        
        Returns:
            A JSON response from the server after updating project settings.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request fails or returns an error status code.
        
        Tags:
            update, project, settings, management, enterprise, important
        """
        request_body = {
            "sharingPolicySettings": sharingPolicySettings,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_of_project_members(self, cursor: Annotated[Any, 'An indicator of the position of a page in the full set of results. To obtain the first page leave it empty. To obtain subsequent pages set it to the value returned in the cursor field of the previous request.'] = None, limit: Annotated[Any, 'The maximum number of results to return per call. If the number of project members in the response is greater than the limit specified, the response returns the cursor parameter with a value.'] = None) -> Any:
        """
        Retrieves a paginated list of members for a specific project, supporting cursor-based pagination.
        
        Args:
            cursor: An indicator of the position of a page in the full set of results. Leave empty to fetch the first page, or use the value from the previous response's 'cursor' field for subsequent pages.
            limit: The maximum number of results per request. If the response contains more members than this limit, the 'cursor' parameter is included in the response.
        
        Returns:
            A JSON response containing the list of project members and pagination metadata, including a cursor for subsequent requests when applicable.
        
        Raises:
            HTTPError: Raised when the API request fails, typically due to authentication errors, invalid parameters, or rate limiting.
        
        Tags:
            list, project-members, pagination, async-job, important, management
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "cursor": cursor,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def add_member_in_aproject(self, email: Annotated[Any, ''] = None, role: Annotated[Any, ''] = None) -> Any:
        """
        Adds a member to a project by sending a request with the member's email and role.
        
        Args:
            email: Email of the user to be added to the project
            role: Role of the user in the project
        
        Returns:
            JSON response from the API indicating the result of the operation
        
        Raises:
            HTTPError: Raised if the HTTP request fails, such as due to invalid credentials or rate limiting.
        
        Tags:
            add, project-members, management, important
        """
        request_body = {
            "email": email,
            "role": role,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_project_member(self, ) -> Any:
        """
        Retrieves information for a specific project member from Miro. Requires Company Admin role and Enterprise plan access.
        
        Returns:
            dict: A JSON response containing the project member's details.
        
        Raises:
            HTTPError: Raised when the API request fails, typically due to insufficient permissions, invalid authentication (status 401/403), rate limiting, or API errors (status 400/404/500).
        
        Tags:
            get, project-members, enterprise, important, async_job
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def remove_project_member(self, ) -> Any:
        """
        Remove a project member from a project without removing them from the team.
        
        Args:
            None: This function does not take any parameters.
        
        Returns:
            The response from the server after removing the project member.
        
        Raises:
            requests.exceptions.HTTPError: Raised when the HTTP request returns an unsuccessful status code.
        
        Tags:
            remove, project, management, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_project_member(self, role: Annotated[Any, ''] = None) -> Any:
        """
        Updates the role of a project member.
        
        Args:
            role: New role to assign to the project member.
        
        Returns:
            Dictionary containing the updated project member details (if available) from the server response.
        
        Raises:
            HTTPError: If the API request fails due to server errors (4XX/5XX) or invalid permissions.
        
        Tags:
            update, project-members, role-management, enterprise, api, important
        """
        request_body = {
            "role": role,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_teams(self, cursor: Annotated[Any, 'An indicator of the position of a page in the full set of results. To obtain the first page leave it empty. To obtain subsequent pages set it to the value returned in the cursor field of the previous request.'] = None, limit: Annotated[Any, ''] = None, name: Annotated[Any, 'Name query. Filters teams by name using case insensitive partial match. A value "dev" will return both "Developer\'s team" and "Team for developers".'] = None) -> Any:
        """
        Retrieves a paginated list of teams in an organization, filtered by name if provided.
        
        Args:
            cursor: An indicator of pagination position. Leave empty for the first page, or use the value from the previous response's cursor field for subsequent pages.
            limit: Maximum number of teams to retrieve (exact behavior depends on API implementation details).
            name: Case-insensitive partial match filter for team names (e.g., 'dev' matches 'Developer\'s team' and 'Developers').
        
        Returns:
            API response JSON containing teams data and pagination information.
        
        Raises:
            HTTPError: When the API request fails due to network issues, invalid parameters, or insufficient permissions.
        
        Tags:
            list-teams, pagination, filter, enterprise, management, teams, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "cursor": cursor,
                "name": name,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def create_team(self, name: Annotated[Any, ''] = None) -> Any:
        """
        Creates a new team in an existing organization with the specified name.
        
        Args:
            name: (Annotated[Any, '']) The name of the team to create. Must be a non-empty string if required by API constraints, although the type annotation currently allows any value.
        
        Returns:
            dict: A dictionary containing the newly created team's data as returned by the Miro API.
        
        Raises:
            HTTPError: If the API request fails (e.g., invalid credentials, rate limiting, or insufficient permissions). Raised by response.raise_for_status().
        
        Tags:
            teams, create, management, api, enterprise, important
        """
        request_body = {
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_team(self, ) -> Any:
        """
        Retrieves team information for an existing team, available for Enterprise plan users.
        
        Returns:
            JSON response containing team information.
        
        Raises:
            HTTPError: Raised if the HTTP request encounters an unexpected status code.
        
        Tags:
            teams, enterprise, management, read, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_team(self, ) -> Any:
        """
        Delete an existing team from the Miro organization, requiring Company Admin privileges and Enterprise plan access.
        
        Args:
            None: This function does not require direct parameters as it acts on the current instance's context and API configuration.
        
        Returns:
            JSON response from the Miro API containing deletion confirmation details.
        
        Raises:
            HTTPError: If the API request fails due to invalid permissions, missing team, or rate limits (Level 4). Raised by response.raise_for_status().
        
        Tags:
            delete, teams, management, enterprise, async_job, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_team(self, name: Annotated[Any, ''] = None) -> Any:
        """
        Updates an existing team by changing its name.
        
        Args:
            name: The new name of the team; if None, no change is made.
        
        Returns:
            The JSON response from the server after updating the team.
        
        Raises:
            HTTPError: Raised if there is an HTTP request error, such as a bad status code.
        
        Tags:
            update, team, management, enterprise, important
        """
        request_body = {
            "name": name,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def list_team_members(self, cursor: Annotated[Any, 'An indicator of the position of a page in the full set of results. To obtain the first page leave it empty. To obtain subsequent pages set it to the value returned in the cursor field of the previous request.'] = None, limit: Annotated[Any, ''] = None, role: Annotated[Any, '\nRole query. Filters members by role using full word match. Accepted values are:\n* "member":     Team member with full member permissions.\n* "admin":      Admin of a team. Team member with permission to manage team.\n* "non_team":   External user, non-team user.\n* "team_guest": Team-guest user, user with access only to a team without access to organization.\n'] = None) -> Any:
        """
        Retrieves team members with pagination and optional role filtering, requiring specific permissions and rate limits.
        
        Args:
            cursor: An indicator of the page position in results. Leave empty for first page, use previous response's cursor for subsequent pages.
            limit: Maximum number of team members to retrieve per request. If unspecified, uses API's default parameter value.
            role: Role filter (full-word match): 'member' (full permissions), 'admin' (team management), 'non_team' (external users), 'team_guest' (team-only access).
        
        Returns:
            JSON response containing paginated team members and next-page cursor.
        
        Raises:
            HTTPError: If the API request fails due to invalid permissions, rate limits, or server errors.
        
        Tags:
            list, team-members, pagination, management, enterprise, api, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {
                "limit": limit,
                "cursor": cursor,
                "role": role,
            }
        query_params = {k: v for k, v in query_params.items() if v is not None}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def invite_team_members(self, email: Annotated[Any, ''] = None, role: Annotated[Any, ''] = None) -> Any:
        """
        Invites a new Miro user to an existing team via email, requiring the user to exist in the organization (team invites via SCIM/external identity providers require separate implementation).
        
        Args:
            email: Email address of the user to invite (must already exist in organization)
            role: Team role to assign to invited member
        
        Returns:
            API response data containing invitation details
        
        Raises:
            requests.HTTPError: Raised for HTTP request failures (e.g., invalid scope, unauthorized access, or rate limit exceeded)
        
        Tags:
            team-members, invite, management, enterprise, important
        """
        request_body = {
            "email": email,
            "role": role,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._post(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_team_member(self, ) -> Any:
        """
        Retrieves a team member.
        
        Args:
            None: This function does not take any parameters.
        
        Returns:
            A JSON response containing the team member details.
        
        Raises:
            requests.exceptions.HTTPError: Raised if the HTTP request encounters an error, such as a 4xx or 5xx status code.
        
        Tags:
            retrieve, team-member, enterprise, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def delete_team_member_from_team(self, ) -> Any:
        """
        Deletes a team member from a team (Note: Currently no parameters are defined to identify the member/team for deletion).
        
        Args:
            None: This function currently takes no parameters.
        
        Returns:
            The JSON response from the delete operation.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request encounters an error (e.g., 404 Not Found, 500 Internal Server Error).
        
        Tags:
            delete, team-member, enterprise-only, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._delete(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_team_member(self, role: Annotated[Any, ''] = None) -> Any:
        """
        Updates the role of a team member within an organization, requiring Company Admin permissions and a specific scope.
        
        Args:
            role: New role to assign to the team member. Must comply with organizational role definitions.
        
        Returns:
            dict: Updated team member data from the API response after successful role modification.
        
        Raises:
            HTTPError: If the API request fails due to insufficient permissions, invalid role, or authorization issues.
        
        Tags:
            update, team-members, management, enterprise-only, important, async-job, api-call
        """
        request_body = {
            "role": role,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_default_team_settings(self, ) -> Any:
        """
        Retrieve default team settings for an existing organization. Requires Company Admin privileges.
        
        Returns:
            dict: Default team settings parsed from the API response JSON.
        
        Raises:
            requests.HTTPError: If the API request fails due to invalid scope, insufficient permissions, or rate limits.
        
        Tags:
            team-settings, management, enterprise, api, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def get_team_settings1(self, ) -> Any:
        """
        Retrieves team settings for an existing team. Requires enterprise plan and Company Admin role.
        
        Args:
            None: This function takes no arguments
        
        Returns:
            dict: JSON response containing team settings
        
        Raises:
            requests.exceptions.HTTPError: Raised if the API request fails (e.g., unauthorized access or invalid endpoint)
        
        Tags:
            get, team-settings, read, management, enterprise, important
        """
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._get(url, params=query_params)
        response.raise_for_status()
        return response.json()

    def update_team_settings1(self, teamAccountDiscoverySettings: Annotated[dict[str, Any], ''] = None, teamCollaborationSettings: Annotated[dict[str, Any], ''] = None, teamCopyAccessLevelSettings: Annotated[dict[str, Any], ''] = None, teamInvitationSettings: Annotated[dict[str, Any], ''] = None, teamSharingPolicySettings: Annotated[dict[str, Any], ''] = None) -> Any:
        """
        Updates team settings for an existing team.
        
        Args:
            teamAccountDiscoverySettings: A dictionary containing team account discovery settings.
            teamCollaborationSettings: A dictionary containing team collaboration settings.
            teamCopyAccessLevelSettings: A dictionary containing team copy access level settings.
            teamInvitationSettings: A dictionary containing team invitation settings.
            teamSharingPolicySettings: A dictionary containing team sharing policy settings.
        
        Returns:
            The updated team settings in JSON format.
        
        Raises:
            requests.HTTPError: Raised if the HTTP request fails due to a network problem or the server returns an unsuccessful status code.
        
        Tags:
            update, team-settings, enterprise, important
        """
        request_body = {
            "teamAccountDiscoverySettings": teamAccountDiscoverySettings,
            "teamCollaborationSettings": teamCollaborationSettings,
            "teamCopyAccessLevelSettings": teamCopyAccessLevelSettings,
            "teamInvitationSettings": teamInvitationSettings,
            "teamSharingPolicySettings": teamSharingPolicySettings,
        }
        request_body = {k: v for k, v in request_body.items() if v is not None}
        path = ""
        url = f"{self.base_url}{path}"
        query_params = {}
        response = self._patch(url, data=request_body, params=query_params)
        response.raise_for_status()
        return response.json()


    def list_tools(self):
        return [
            
            self.revoke_token_v1,
            self.get_access_token_information,
            self.get_audit_logs,
            self.get_organization_settings,
            self.bulk_update_boards_classification,
            self.get_team_settings,
            self.update_team_settings,
            self.get_board_classification,
            self.update_board_classification,
            self.get_all_cases,
            self.get_case,
            self.get_all_legal_holds_within_acase,
            self.get_legal_hold_information,
            self.get_content_items_under_legal_hold,
            self.create_board_export_job,
            self.get_board_export_job_status,
            self.get_results_for_board_export_job,
            self.retrieve_content_change_logs_of_board_items,
            self.reset_all_sessions_of_auser,
            self.get_organization_info,
            self.get_organization_members,
            self.get_organization_member,
            self.get_boards,
            self.copy_board,
            self.create_board,
            self.get_specific_board,
            self.delete_board,
            self.update_board,
            self.create_app_card_item,
            self.get_app_card_item,
            self.delete_app_card_item,
            self.update_app_card_item,
            self.create_card_item,
            self.get_card_item,
            self.delete_card_item,
            self.update_card_item,
            self.get_connectors,
            self.create_connector,
            self.get_specific_connector,
            self.delete_connector,
            self.update_connector,
            self.create_document_item_using_url,
            self.get_document_item,
            self.delete_document_item,
            self.update_document_item_using_url,
            self.create_document_item_using_file_from_device,
            self.update_document_item_using_file_from_device,
            self.create_embed_item,
            self.get_embed_item,
            self.delete_embed_item,
            self.update_embed_item,
            self.create_image_item_using_url,
            self.get_image_item,
            self.delete_image_item,
            self.update_image_item_using_url,
            self.create_image_item_using_file_from_device,
            self.update_image_item_using_file_from_device,
            self.get_items_on_board,
            self.get_specific_item_on_board,
            self.delete_item,
            self.update_item_position_or_parent,
            self.get_items_within_frame,
            self.get_specific_item_on_board1,
            self.delete_item1,
            self.get_all_board_members,
            self.share_board,
            self.get_specific_board_member,
            self.remove_board_member,
            self.update_board_member,
            self.create_shape_item,
            self.get_shape_item,
            self.delete_shape_item,
            self.update_shape_item,
            self.create_sticky_note_item,
            self.get_sticky_note_item,
            self.delete_sticky_note_item,
            self.update_sticky_note_item,
            self.create_text_item,
            self.get_text_item,
            self.delete_text_item,
            self.update_text_item,
            self.create_items_in_bulk,
            self.create_items_in_bulk_using_file_from_device,
            self.create_frame,
            self.get_frame,
            self.delete_frame,
            self.update_frame,
            self.get_app_metrics,
            self.get_total_app_metrics,
            self.create_webhook_subscription,
            self.update_webhook_subscription,
            self.get_webhook_subscriptions,
            self.get_specific_webhook_subscription,
            self.delete_webhook_subscription,
            self.get_specific_mind_map_node,
            self.delete_mind_map_node,
            self.get_mind_map_nodes,
            self.create_mind_map_node,
            self.get_items_on_board1,
            self.create_shape_item1,
            self.get_shape_item1,
            self.delete_shape_item1,
            self.update_shape_item1,
            self.get_all_groups_on_aboard,
            self.create_group,
            self.get_items_of_agroup_by_id,
            self.get_agroup_by_its_id,
            self.updates_agroup_with_new_items,
            self.ungroup_items,
            self.deletes_the_group,
            self.revoke_token_v2,
            self.get_tags_from_item,
            self.get_tags_from_board,
            self.create_tag,
            self.get_tag,
            self.delete_tag,
            self.update_tag,
            self.get_items_by_tag,
            self.attach_tag_to_item,
            self.remove_tag_from_item,
            self.list_of_projects,
            self.create_project,
            self.get_project,
            self.delete_project,
            self.update_project,
            self.get_project_settings,
            self.update_project_settings,
            self.list_of_project_members,
            self.add_member_in_aproject,
            self.get_project_member,
            self.remove_project_member,
            self.update_project_member,
            self.list_teams,
            self.create_team,
            self.get_team,
            self.delete_team,
            self.update_team,
            self.list_team_members,
            self.invite_team_members,
            self.get_team_member,
            self.delete_team_member_from_team,
            self.update_team_member,
            self.get_default_team_settings,
            self.get_team_settings1,
            self.update_team_settings1
        ] 