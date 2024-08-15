# coding: utf-8

# flake8: noqa
"""
    codebeamer swagger API

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 3.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


# import models into model package
from openapi_client.models.abstract_background_job_status_info import AbstractBackgroundJobStatusInfo
from openapi_client.models.abstract_baseline_reference_model import AbstractBaselineReferenceModel
from openapi_client.models.abstract_field import AbstractField
from openapi_client.models.abstract_field_value import AbstractFieldValue
from openapi_client.models.abstract_outline import AbstractOutline
from openapi_client.models.abstract_reference import AbstractReference
from openapi_client.models.abstract_tracker_item_change import AbstractTrackerItemChange
from openapi_client.models.abstract_tracker_item_reference import AbstractTrackerItemReference
from openapi_client.models.access_permission import AccessPermission
from openapi_client.models.access_permissions_request import AccessPermissionsRequest
from openapi_client.models.artifact_reference import ArtifactReference
from openapi_client.models.artifact_reference_field import ArtifactReferenceField
from openapi_client.models.artifact_revision import ArtifactRevision
from openapi_client.models.artifact_revision_search_result import ArtifactRevisionSearchResult
from openapi_client.models.association import Association
from openapi_client.models.association_type import AssociationType
from openapi_client.models.association_type_reference import AssociationTypeReference
from openapi_client.models.attachment import Attachment
from openapi_client.models.attachment_migration_request import AttachmentMigrationRequest
from openapi_client.models.attachment_reference import AttachmentReference
from openapi_client.models.attachment_search_result import AttachmentSearchResult
from openapi_client.models.auto_apply_test_step_reuses import AutoApplyTestStepReuses
from openapi_client.models.automated_test_case_run_result import AutomatedTestCaseRunResult
from openapi_client.models.automated_test_run_request import AutomatedTestRunRequest
from openapi_client.models.background_job import BackgroundJob
from openapi_client.models.background_job_step import BackgroundJobStep
from openapi_client.models.bad_request_exception import BadRequestException
from openapi_client.models.base_tracker_field_choice_option import BaseTrackerFieldChoiceOption
from openapi_client.models.base_tracker_field_permission import BaseTrackerFieldPermission
from openapi_client.models.baseline import Baseline
from openapi_client.models.batch_get_tracker_item_reviews_request import BatchGetTrackerItemReviewsRequest
from openapi_client.models.bool_field import BoolField
from openapi_client.models.bool_field_value import BoolFieldValue
from openapi_client.models.branch_reference import BranchReference
from openapi_client.models.bulk_operation_response import BulkOperationResponse
from openapi_client.models.choice_documents import ChoiceDocuments
from openapi_client.models.choice_field_multi_value import ChoiceFieldMultiValue
from openapi_client.models.choice_field_value import ChoiceFieldValue
from openapi_client.models.choice_members import ChoiceMembers
from openapi_client.models.choice_option_reference import ChoiceOptionReference
from openapi_client.models.choice_options import ChoiceOptions
from openapi_client.models.choice_options_choice_option import ChoiceOptionsChoiceOption
from openapi_client.models.choice_projects import ChoiceProjects
from openapi_client.models.choice_repositories import ChoiceRepositories
from openapi_client.models.choice_trackers import ChoiceTrackers
from openapi_client.models.choice_users import ChoiceUsers
from openapi_client.models.choice_work_config_items import ChoiceWorkConfigItems
from openapi_client.models.color_field import ColorField
from openapi_client.models.color_field_value import ColorFieldValue
from openapi_client.models.comment import Comment
from openapi_client.models.comment_reference import CommentReference
from openapi_client.models.country_field import CountryField
from openapi_client.models.country_field_multi_value import CountryFieldMultiValue
from openapi_client.models.country_field_value import CountryFieldValue
from openapi_client.models.create_baseline_request import CreateBaselineRequest
from openapi_client.models.create_test_run_from_test_sets_request import CreateTestRunFromTestSetsRequest
from openapi_client.models.create_test_run_request import CreateTestRunRequest
from openapi_client.models.cross_project_dependency import CrossProjectDependency
from openapi_client.models.date_field import DateField
from openapi_client.models.date_field_value import DateFieldValue
from openapi_client.models.decimal_field import DecimalField
from openapi_client.models.decimal_field_value import DecimalFieldValue
from openapi_client.models.default_background_job_status_info import DefaultBackgroundJobStatusInfo
from openapi_client.models.dependency_attribute import DependencyAttribute
from openapi_client.models.dependency_entity_reference import DependencyEntityReference
from openapi_client.models.dependency_finder_job_status_info import DependencyFinderJobStatusInfo
from openapi_client.models.deploy_project import DeployProject
from openapi_client.models.deployment_project_export_settings import DeploymentProjectExportSettings
from openapi_client.models.deployment_tracker_export_settings import DeploymentTrackerExportSettings
from openapi_client.models.downstream_tracker_item_reference import DownstreamTrackerItemReference
from openapi_client.models.duration_field import DurationField
from openapi_client.models.duration_field_value import DurationFieldValue
from openapi_client.models.export_for_deployment_request import ExportForDeploymentRequest
from openapi_client.models.export_project import ExportProject
from openapi_client.models.export_to_word_request import ExportToWordRequest
from openapi_client.models.failed_operation import FailedOperation
from openapi_client.models.field_layout_groups import FieldLayoutGroups
from openapi_client.models.field_layout_settings import FieldLayoutSettings
from openapi_client.models.field_reference import FieldReference
from openapi_client.models.incoming_tracker_item_association import IncomingTrackerItemAssociation
from openapi_client.models.integer_field import IntegerField
from openapi_client.models.integer_field_value import IntegerFieldValue
from openapi_client.models.internal_server_error_exception import InternalServerErrorException
from openapi_client.models.invalid_parameters_exception import InvalidParametersException
from openapi_client.models.job_reference import JobReference
from openapi_client.models.json_view import JsonView
from openapi_client.models.label import Label
from openapi_client.models.language_field import LanguageField
from openapi_client.models.language_field_multi_value import LanguageFieldMultiValue
from openapi_client.models.language_field_value import LanguageFieldValue
from openapi_client.models.layout_field import LayoutField
from openapi_client.models.lock_info import LockInfo
from openapi_client.models.lock_request import LockRequest
from openapi_client.models.maintenance_mode import MaintenanceMode
from openapi_client.models.maintenance_mode_properties import MaintenanceModeProperties
from openapi_client.models.member_field import MemberField
from openapi_client.models.member_reference_search_result import MemberReferenceSearchResult
from openapi_client.models.not_implemented_exception import NotImplementedException
from openapi_client.models.not_supported_field_value import NotSupportedFieldValue
from openapi_client.models.option_choice_field import OptionChoiceField
from openapi_client.models.outgoing_tracker_item_association import OutgoingTrackerItemAssociation
from openapi_client.models.outline_index import OutlineIndex
from openapi_client.models.outline_item import OutlineItem
from openapi_client.models.outline_item_search_result import OutlineItemSearchResult
from openapi_client.models.outline_wiki import OutlineWiki
from openapi_client.models.per_status_field_permission import PerStatusFieldPermission
from openapi_client.models.permission_ids_request import PermissionIdsRequest
from openapi_client.models.project import Project
from openapi_client.models.project_baseline_reference import ProjectBaselineReference
from openapi_client.models.project_choice_field import ProjectChoiceField
from openapi_client.models.project_filtering_request import ProjectFilteringRequest
from openapi_client.models.project_member_permissions import ProjectMemberPermissions
from openapi_client.models.project_reference import ProjectReference
from openapi_client.models.project_role_reference import ProjectRoleReference
from openapi_client.models.project_search_result import ProjectSearchResult
from openapi_client.models.reference_field import ReferenceField
from openapi_client.models.reference_filter_based_choice_reference_filter import ReferenceFilterBasedChoiceReferenceFilter
from openapi_client.models.reference_search_result import ReferenceSearchResult
from openapi_client.models.referred_test_step_field_value import ReferredTestStepFieldValue
from openapi_client.models.remote_migration_file import RemoteMigrationFile
from openapi_client.models.report_aggregate import ReportAggregate
from openapi_client.models.report_cell import ReportCell
from openapi_client.models.report_column import ReportColumn
from openapi_client.models.report_column_settings import ReportColumnSettings
from openapi_client.models.report_group import ReportGroup
from openapi_client.models.report_group_with_groups import ReportGroupWithGroups
from openapi_client.models.report_group_with_referenced_rows import ReportGroupWithReferencedRows
from openapi_client.models.report_group_with_rows import ReportGroupWithRows
from openapi_client.models.report_item import ReportItem
from openapi_client.models.report_item_reference import ReportItemReference
from openapi_client.models.report_item_result import ReportItemResult
from openapi_client.models.report_paging_information import ReportPagingInformation
from openapi_client.models.report_permission import ReportPermission
from openapi_client.models.report_reference import ReportReference
from openapi_client.models.report_reference_level import ReportReferenceLevel
from openapi_client.models.report_reference_level_settings import ReportReferenceLevelSettings
from openapi_client.models.report_referenced_row import ReportReferencedRow
from openapi_client.models.report_result import ReportResult
from openapi_client.models.report_row import ReportRow
from openapi_client.models.repository_choice_field import RepositoryChoiceField
from openapi_client.models.repository_reference import RepositoryReference
from openapi_client.models.resizable_report_column_settings import ResizableReportColumnSettings
from openapi_client.models.resource_forbidden_exception import ResourceForbiddenException
from openapi_client.models.resource_locked_exception import ResourceLockedException
from openapi_client.models.resource_not_found_exception import ResourceNotFoundException
from openapi_client.models.resource_unauthorized_exception import ResourceUnauthorizedException
from openapi_client.models.rest_exception import RestException
from openapi_client.models.review_member_reference_field import ReviewMemberReferenceField
from openapi_client.models.role import Role
from openapi_client.models.role_reference import RoleReference
from openapi_client.models.role_with_permissions import RoleWithPermissions
from openapi_client.models.same_as_field_permission import SameAsFieldPermission
from openapi_client.models.shared_field_reference import SharedFieldReference
from openapi_client.models.simple_report_settings import SimpleReportSettings
from openapi_client.models.single_field_permission import SingleFieldPermission
from openapi_client.models.status_layout import StatusLayout
from openapi_client.models.system_status import SystemStatus
from openapi_client.models.table_field import TableField
from openapi_client.models.table_field_value import TableFieldValue
from openapi_client.models.test_run_result import TestRunResult
from openapi_client.models.text_field import TextField
from openapi_client.models.text_field_value import TextFieldValue
from openapi_client.models.too_many_requests_exception import TooManyRequestsException
from openapi_client.models.traceability_initial_level_filter import TraceabilityInitialLevelFilter
from openapi_client.models.traceability_item import TraceabilityItem
from openapi_client.models.traceability_level_filter import TraceabilityLevelFilter
from openapi_client.models.traceability_result import TraceabilityResult
from openapi_client.models.tracker import Tracker
from openapi_client.models.tracker_baseline_reference import TrackerBaselineReference
from openapi_client.models.tracker_basic_information import TrackerBasicInformation
from openapi_client.models.tracker_choice_field import TrackerChoiceField
from openapi_client.models.tracker_configuration import TrackerConfiguration
from openapi_client.models.tracker_field import TrackerField
from openapi_client.models.tracker_field_computed_field_reference import TrackerFieldComputedFieldReference
from openapi_client.models.tracker_field_date_field_settings import TrackerFieldDateFieldSettings
from openapi_client.models.tracker_field_dependency import TrackerFieldDependency
from openapi_client.models.tracker_field_layout_settings import TrackerFieldLayoutSettings
from openapi_client.models.tracker_field_permission_access_permission import TrackerFieldPermissionAccessPermission
from openapi_client.models.tracker_field_permissions import TrackerFieldPermissions
from openapi_client.models.tracker_field_service_desk_field import TrackerFieldServiceDeskField
from openapi_client.models.tracker_field_status_permissions import TrackerFieldStatusPermissions
from openapi_client.models.tracker_fields_status_permissions import TrackerFieldsStatusPermissions
from openapi_client.models.tracker_filtering_request import TrackerFilteringRequest
from openapi_client.models.tracker_item import TrackerItem
from openapi_client.models.tracker_item_attachment_request import TrackerItemAttachmentRequest
from openapi_client.models.tracker_item_change import TrackerItemChange
from openapi_client.models.tracker_item_child_reference import TrackerItemChildReference
from openapi_client.models.tracker_item_choice_field import TrackerItemChoiceField
from openapi_client.models.tracker_item_field import TrackerItemField
from openapi_client.models.tracker_item_field_accessibility import TrackerItemFieldAccessibility
from openapi_client.models.tracker_item_field_accessibility_list import TrackerItemFieldAccessibilityList
from openapi_client.models.tracker_item_field_mapping import TrackerItemFieldMapping
from openapi_client.models.tracker_item_field_mapping_info import TrackerItemFieldMappingInfo
from openapi_client.models.tracker_item_field_mapping_pair import TrackerItemFieldMappingPair
from openapi_client.models.tracker_item_field_mapping_possible_pair import TrackerItemFieldMappingPossiblePair
from openapi_client.models.tracker_item_history import TrackerItemHistory
from openapi_client.models.tracker_item_history_revision import TrackerItemHistoryRevision
from openapi_client.models.tracker_item_move_request import TrackerItemMoveRequest
from openapi_client.models.tracker_item_reference import TrackerItemReference
from openapi_client.models.tracker_item_reference_data import TrackerItemReferenceData
from openapi_client.models.tracker_item_reference_search_result import TrackerItemReferenceSearchResult
from openapi_client.models.tracker_item_relations_result import TrackerItemRelationsResult
from openapi_client.models.tracker_item_review import TrackerItemReview
from openapi_client.models.tracker_item_review_config import TrackerItemReviewConfig
from openapi_client.models.tracker_item_review_export import TrackerItemReviewExport
from openapi_client.models.tracker_item_review_vote import TrackerItemReviewVote
from openapi_client.models.tracker_item_review_vote_export import TrackerItemReviewVoteExport
from openapi_client.models.tracker_item_revision import TrackerItemRevision
from openapi_client.models.tracker_item_row_change import TrackerItemRowChange
from openapi_client.models.tracker_item_search_request import TrackerItemSearchRequest
from openapi_client.models.tracker_item_search_result import TrackerItemSearchResult
from openapi_client.models.tracker_item_with_tracker_item_reviews_export import TrackerItemWithTrackerItemReviewsExport
from openapi_client.models.tracker_items_request import TrackerItemsRequest
from openapi_client.models.tracker_permission import TrackerPermission
from openapi_client.models.tracker_permission_reference import TrackerPermissionReference
from openapi_client.models.tracker_reference import TrackerReference
from openapi_client.models.tracker_report_settings import TrackerReportSettings
from openapi_client.models.tracker_search_result import TrackerSearchResult
from openapi_client.models.tracker_tree import TrackerTree
from openapi_client.models.tracker_type import TrackerType
from openapi_client.models.tracker_type_reference import TrackerTypeReference
from openapi_client.models.tracker_working_set import TrackerWorkingSet
from openapi_client.models.unrestricted_field_permission import UnrestrictedFieldPermission
from openapi_client.models.update_test_case_run_request import UpdateTestCaseRunRequest
from openapi_client.models.update_test_run_request import UpdateTestRunRequest
from openapi_client.models.update_tracker_item_children_request import UpdateTrackerItemChildrenRequest
from openapi_client.models.update_tracker_item_field import UpdateTrackerItemField
from openapi_client.models.update_tracker_item_field_with_item_id import UpdateTrackerItemFieldWithItemId
from openapi_client.models.update_tracker_item_table_field import UpdateTrackerItemTableField
from openapi_client.models.upstream_tracker_item_reference import UpstreamTrackerItemReference
from openapi_client.models.url_field import UrlField
from openapi_client.models.url_field_value import UrlFieldValue
from openapi_client.models.user import User
from openapi_client.models.user_choice_field import UserChoiceField
from openapi_client.models.user_filtering_request import UserFilteringRequest
from openapi_client.models.user_group import UserGroup
from openapi_client.models.user_group_reference import UserGroupReference
from openapi_client.models.user_reference import UserReference
from openapi_client.models.user_reference_search_result import UserReferenceSearchResult
from openapi_client.models.user_search_result import UserSearchResult
from openapi_client.models.wiki_outline_search_result import WikiOutlineSearchResult
from openapi_client.models.wiki_page import WikiPage
from openapi_client.models.wiki_page_reference import WikiPageReference
from openapi_client.models.wiki_render_request import WikiRenderRequest
from openapi_client.models.wiki_text_field import WikiTextField
from openapi_client.models.wiki_text_field_multi_value import WikiTextFieldMultiValue
from openapi_client.models.wiki_text_field_value import WikiTextFieldValue
from openapi_client.models.workflow_transition import WorkflowTransition
from openapi_client.models.working_set_information import WorkingSetInformation
from openapi_client.models.working_set_item_mapping import WorkingSetItemMapping
from openapi_client.models.working_set_items_mapping_request import WorkingSetItemsMappingRequest
from openapi_client.models.working_set_minimal import WorkingSetMinimal
from openapi_client.models.working_set_permission_request import WorkingSetPermissionRequest
from openapi_client.models.working_set_reference import WorkingSetReference
from openapi_client.models.working_set_tracker import WorkingSetTracker
from openapi_client.models.working_set_tracker_update_request import WorkingSetTrackerUpdateRequest
from openapi_client.models.working_set_update_request import WorkingSetUpdateRequest