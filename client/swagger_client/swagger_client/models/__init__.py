# coding: utf-8

# flake8: noqa
"""
    codebeamer swagger API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 3.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import models into model package
from swagger_client.models.abstract_background_job_status_info import AbstractBackgroundJobStatusInfo
from swagger_client.models.abstract_baseline_reference_model import AbstractBaselineReferenceModel
from swagger_client.models.abstract_field import AbstractField
from swagger_client.models.abstract_field_value import AbstractFieldValue
from swagger_client.models.abstract_outline import AbstractOutline
from swagger_client.models.abstract_reference import AbstractReference
from swagger_client.models.abstract_tracker_item_change import AbstractTrackerItemChange
from swagger_client.models.abstract_tracker_item_reference import AbstractTrackerItemReference
from swagger_client.models.access_permission import AccessPermission
from swagger_client.models.access_permissions_request import AccessPermissionsRequest
from swagger_client.models.artifact_reference import ArtifactReference
from swagger_client.models.artifact_reference_field import ArtifactReferenceField
from swagger_client.models.artifact_revision import ArtifactRevision
from swagger_client.models.artifact_revision_search_result import ArtifactRevisionSearchResult
from swagger_client.models.association import Association
from swagger_client.models.association_type import AssociationType
from swagger_client.models.association_type_reference import AssociationTypeReference
from swagger_client.models.attachment import Attachment
from swagger_client.models.attachment_migration_request import AttachmentMigrationRequest
from swagger_client.models.attachment_reference import AttachmentReference
from swagger_client.models.attachment_search_result import AttachmentSearchResult
from swagger_client.models.auto_apply_test_step_reuses import AutoApplyTestStepReuses
from swagger_client.models.automated_test_case_run_result import AutomatedTestCaseRunResult
from swagger_client.models.automated_test_run_request import AutomatedTestRunRequest
from swagger_client.models.background_job import BackgroundJob
from swagger_client.models.background_job_step import BackgroundJobStep
from swagger_client.models.bad_request_exception import BadRequestException
from swagger_client.models.base_tracker_field_choice_option import BaseTrackerFieldChoiceOption
from swagger_client.models.base_tracker_field_permission import BaseTrackerFieldPermission
from swagger_client.models.baseline import Baseline
from swagger_client.models.batch_get_tracker_item_reviews_request import BatchGetTrackerItemReviewsRequest
from swagger_client.models.bool_field import BoolField
from swagger_client.models.bool_field_value import BoolFieldValue
from swagger_client.models.branch_reference import BranchReference
from swagger_client.models.bulk_operation_response import BulkOperationResponse
from swagger_client.models.choice_documents import ChoiceDocuments
from swagger_client.models.choice_field_multi_value import ChoiceFieldMultiValue
from swagger_client.models.choice_field_value import ChoiceFieldValue
from swagger_client.models.choice_members import ChoiceMembers
from swagger_client.models.choice_option_reference import ChoiceOptionReference
from swagger_client.models.choice_options import ChoiceOptions
from swagger_client.models.choice_options_choice_option import ChoiceOptionsChoiceOption
from swagger_client.models.choice_projects import ChoiceProjects
from swagger_client.models.choice_repositories import ChoiceRepositories
from swagger_client.models.choice_trackers import ChoiceTrackers
from swagger_client.models.choice_users import ChoiceUsers
from swagger_client.models.choice_work_config_items import ChoiceWorkConfigItems
from swagger_client.models.color_field import ColorField
from swagger_client.models.color_field_value import ColorFieldValue
from swagger_client.models.comment import Comment
from swagger_client.models.comment_reference import CommentReference
from swagger_client.models.country_field import CountryField
from swagger_client.models.country_field_multi_value import CountryFieldMultiValue
from swagger_client.models.country_field_value import CountryFieldValue
from swagger_client.models.create_baseline_request import CreateBaselineRequest
from swagger_client.models.create_test_run_from_test_sets_request import CreateTestRunFromTestSetsRequest
from swagger_client.models.create_test_run_request import CreateTestRunRequest
from swagger_client.models.cross_project_dependency import CrossProjectDependency
from swagger_client.models.date_field import DateField
from swagger_client.models.date_field_value import DateFieldValue
from swagger_client.models.decimal_field import DecimalField
from swagger_client.models.decimal_field_value import DecimalFieldValue
from swagger_client.models.default_background_job_status_info import DefaultBackgroundJobStatusInfo
from swagger_client.models.dependency_attribute import DependencyAttribute
from swagger_client.models.dependency_entity_reference import DependencyEntityReference
from swagger_client.models.dependency_finder_job_status_info import DependencyFinderJobStatusInfo
from swagger_client.models.deploy_project import DeployProject
from swagger_client.models.deployment_model import DeploymentModel
from swagger_client.models.deployment_project_export_settings import DeploymentProjectExportSettings
from swagger_client.models.deployment_tracker_export_settings import DeploymentTrackerExportSettings
from swagger_client.models.downstream_tracker_item_reference import DownstreamTrackerItemReference
from swagger_client.models.duration_field import DurationField
from swagger_client.models.duration_field_value import DurationFieldValue
from swagger_client.models.edit_comment import EditComment
from swagger_client.models.export_for_deployment_request import ExportForDeploymentRequest
from swagger_client.models.export_project import ExportProject
from swagger_client.models.export_to_word_request import ExportToWordRequest
from swagger_client.models.failed_operation import FailedOperation
from swagger_client.models.field_layout_groups import FieldLayoutGroups
from swagger_client.models.field_layout_settings import FieldLayoutSettings
from swagger_client.models.field_reference import FieldReference
from swagger_client.models.incoming_tracker_item_association import IncomingTrackerItemAssociation
from swagger_client.models.integer_field import IntegerField
from swagger_client.models.integer_field_value import IntegerFieldValue
from swagger_client.models.internal_server_error_exception import InternalServerErrorException
from swagger_client.models.invalid_parameters_exception import InvalidParametersException
from swagger_client.models.job_reference import JobReference
from swagger_client.models.json_view import JsonView
from swagger_client.models.label import Label
from swagger_client.models.language_field import LanguageField
from swagger_client.models.language_field_multi_value import LanguageFieldMultiValue
from swagger_client.models.language_field_value import LanguageFieldValue
from swagger_client.models.layout_field import LayoutField
from swagger_client.models.lock_info import LockInfo
from swagger_client.models.lock_request import LockRequest
from swagger_client.models.maintenance_mode import MaintenanceMode
from swagger_client.models.maintenance_mode_properties import MaintenanceModeProperties
from swagger_client.models.member_field import MemberField
from swagger_client.models.member_reference_search_result import MemberReferenceSearchResult
from swagger_client.models.not_implemented_exception import NotImplementedException
from swagger_client.models.not_supported_field_value import NotSupportedFieldValue
from swagger_client.models.option_choice_field import OptionChoiceField
from swagger_client.models.outgoing_tracker_item_association import OutgoingTrackerItemAssociation
from swagger_client.models.outline_index import OutlineIndex
from swagger_client.models.outline_item import OutlineItem
from swagger_client.models.outline_item_search_result import OutlineItemSearchResult
from swagger_client.models.outline_wiki import OutlineWiki
from swagger_client.models.per_status_field_permission import PerStatusFieldPermission
from swagger_client.models.permission_ids_request import PermissionIdsRequest
from swagger_client.models.post_comment import PostComment
from swagger_client.models.project import Project
from swagger_client.models.project_baseline_reference import ProjectBaselineReference
from swagger_client.models.project_choice_field import ProjectChoiceField
from swagger_client.models.project_filtering_request import ProjectFilteringRequest
from swagger_client.models.project_member_permissions import ProjectMemberPermissions
from swagger_client.models.project_reference import ProjectReference
from swagger_client.models.project_role_reference import ProjectRoleReference
from swagger_client.models.project_search_result import ProjectSearchResult
from swagger_client.models.reference_field import ReferenceField
from swagger_client.models.reference_filter_based_choice_reference_filter import ReferenceFilterBasedChoiceReferenceFilter
from swagger_client.models.reference_search_result import ReferenceSearchResult
from swagger_client.models.referred_test_step_field_value import ReferredTestStepFieldValue
from swagger_client.models.remote_migration_file import RemoteMigrationFile
from swagger_client.models.report_aggregate import ReportAggregate
from swagger_client.models.report_cell import ReportCell
from swagger_client.models.report_column import ReportColumn
from swagger_client.models.report_column_settings import ReportColumnSettings
from swagger_client.models.report_group import ReportGroup
from swagger_client.models.report_group_with_groups import ReportGroupWithGroups
from swagger_client.models.report_group_with_referenced_rows import ReportGroupWithReferencedRows
from swagger_client.models.report_group_with_rows import ReportGroupWithRows
from swagger_client.models.report_item import ReportItem
from swagger_client.models.report_item_reference import ReportItemReference
from swagger_client.models.report_item_result import ReportItemResult
from swagger_client.models.report_paging_information import ReportPagingInformation
from swagger_client.models.report_permission import ReportPermission
from swagger_client.models.report_reference import ReportReference
from swagger_client.models.report_reference_level import ReportReferenceLevel
from swagger_client.models.report_reference_level_settings import ReportReferenceLevelSettings
from swagger_client.models.report_referenced_row import ReportReferencedRow
from swagger_client.models.report_result import ReportResult
from swagger_client.models.report_row import ReportRow
from swagger_client.models.repository_choice_field import RepositoryChoiceField
from swagger_client.models.repository_reference import RepositoryReference
from swagger_client.models.resizable_report_column_settings import ResizableReportColumnSettings
from swagger_client.models.resource_forbidden_exception import ResourceForbiddenException
from swagger_client.models.resource_locked_exception import ResourceLockedException
from swagger_client.models.resource_not_found_exception import ResourceNotFoundException
from swagger_client.models.resource_unauthorized_exception import ResourceUnauthorizedException
from swagger_client.models.rest_exception import RestException
from swagger_client.models.review_member_reference_field import ReviewMemberReferenceField
from swagger_client.models.role import Role
from swagger_client.models.role_reference import RoleReference
from swagger_client.models.role_with_permissions import RoleWithPermissions
from swagger_client.models.same_as_field_permission import SameAsFieldPermission
from swagger_client.models.shared_field_reference import SharedFieldReference
from swagger_client.models.simple_report_settings import SimpleReportSettings
from swagger_client.models.single_field_permission import SingleFieldPermission
from swagger_client.models.status_layout import StatusLayout
from swagger_client.models.system_status import SystemStatus
from swagger_client.models.table_field import TableField
from swagger_client.models.table_field_value import TableFieldValue
from swagger_client.models.test_run_result import TestRunResult
from swagger_client.models.text_field import TextField
from swagger_client.models.text_field_value import TextFieldValue
from swagger_client.models.too_many_requests_exception import TooManyRequestsException
from swagger_client.models.traceability_initial_level_filter import TraceabilityInitialLevelFilter
from swagger_client.models.traceability_item import TraceabilityItem
from swagger_client.models.traceability_level_filter import TraceabilityLevelFilter
from swagger_client.models.traceability_result import TraceabilityResult
from swagger_client.models.tracker import Tracker
from swagger_client.models.tracker_baseline_reference import TrackerBaselineReference
from swagger_client.models.tracker_basic_information import TrackerBasicInformation
from swagger_client.models.tracker_choice_field import TrackerChoiceField
from swagger_client.models.tracker_configuration import TrackerConfiguration
from swagger_client.models.tracker_field import TrackerField
from swagger_client.models.tracker_field_computed_field_reference import TrackerFieldComputedFieldReference
from swagger_client.models.tracker_field_date_field_settings import TrackerFieldDateFieldSettings
from swagger_client.models.tracker_field_dependency import TrackerFieldDependency
from swagger_client.models.tracker_field_layout_settings import TrackerFieldLayoutSettings
from swagger_client.models.tracker_field_permission_access_permission import TrackerFieldPermissionAccessPermission
from swagger_client.models.tracker_field_permissions import TrackerFieldPermissions
from swagger_client.models.tracker_field_service_desk_field import TrackerFieldServiceDeskField
from swagger_client.models.tracker_field_status_permissions import TrackerFieldStatusPermissions
from swagger_client.models.tracker_fields_status_permissions import TrackerFieldsStatusPermissions
from swagger_client.models.tracker_filtering_request import TrackerFilteringRequest
from swagger_client.models.tracker_id_icon_body import TrackerIdIconBody
from swagger_client.models.tracker_item import TrackerItem
from swagger_client.models.tracker_item_attachment_request import TrackerItemAttachmentRequest
from swagger_client.models.tracker_item_change import TrackerItemChange
from swagger_client.models.tracker_item_child_reference import TrackerItemChildReference
from swagger_client.models.tracker_item_choice_field import TrackerItemChoiceField
from swagger_client.models.tracker_item_field import TrackerItemField
from swagger_client.models.tracker_item_field_accessibility import TrackerItemFieldAccessibility
from swagger_client.models.tracker_item_field_accessibility_list import TrackerItemFieldAccessibilityList
from swagger_client.models.tracker_item_field_mapping import TrackerItemFieldMapping
from swagger_client.models.tracker_item_field_mapping_info import TrackerItemFieldMappingInfo
from swagger_client.models.tracker_item_field_mapping_pair import TrackerItemFieldMappingPair
from swagger_client.models.tracker_item_field_mapping_possible_pair import TrackerItemFieldMappingPossiblePair
from swagger_client.models.tracker_item_history import TrackerItemHistory
from swagger_client.models.tracker_item_history_revision import TrackerItemHistoryRevision
from swagger_client.models.tracker_item_move_request import TrackerItemMoveRequest
from swagger_client.models.tracker_item_reference import TrackerItemReference
from swagger_client.models.tracker_item_reference_data import TrackerItemReferenceData
from swagger_client.models.tracker_item_reference_search_result import TrackerItemReferenceSearchResult
from swagger_client.models.tracker_item_relations_result import TrackerItemRelationsResult
from swagger_client.models.tracker_item_review import TrackerItemReview
from swagger_client.models.tracker_item_review_config import TrackerItemReviewConfig
from swagger_client.models.tracker_item_review_export import TrackerItemReviewExport
from swagger_client.models.tracker_item_review_vote import TrackerItemReviewVote
from swagger_client.models.tracker_item_review_vote_export import TrackerItemReviewVoteExport
from swagger_client.models.tracker_item_revision import TrackerItemRevision
from swagger_client.models.tracker_item_row_change import TrackerItemRowChange
from swagger_client.models.tracker_item_search_request import TrackerItemSearchRequest
from swagger_client.models.tracker_item_search_result import TrackerItemSearchResult
from swagger_client.models.tracker_item_with_tracker_item_reviews_export import TrackerItemWithTrackerItemReviewsExport
from swagger_client.models.tracker_items_request import TrackerItemsRequest
from swagger_client.models.tracker_permission import TrackerPermission
from swagger_client.models.tracker_permission_reference import TrackerPermissionReference
from swagger_client.models.tracker_reference import TrackerReference
from swagger_client.models.tracker_report_settings import TrackerReportSettings
from swagger_client.models.tracker_search_result import TrackerSearchResult
from swagger_client.models.tracker_tree import TrackerTree
from swagger_client.models.tracker_type import TrackerType
from swagger_client.models.tracker_type_reference import TrackerTypeReference
from swagger_client.models.tracker_working_set import TrackerWorkingSet
from swagger_client.models.unrestricted_field_permission import UnrestrictedFieldPermission
from swagger_client.models.update_attachment import UpdateAttachment
from swagger_client.models.update_test_case_run_request import UpdateTestCaseRunRequest
from swagger_client.models.update_test_run_request import UpdateTestRunRequest
from swagger_client.models.update_tracker_item_children_request import UpdateTrackerItemChildrenRequest
from swagger_client.models.update_tracker_item_field import UpdateTrackerItemField
from swagger_client.models.update_tracker_item_field_with_item_id import UpdateTrackerItemFieldWithItemId
from swagger_client.models.update_tracker_item_table_field import UpdateTrackerItemTableField
from swagger_client.models.upload_attachment import UploadAttachment
from swagger_client.models.upstream_tracker_item_reference import UpstreamTrackerItemReference
from swagger_client.models.url_field import UrlField
from swagger_client.models.url_field_value import UrlFieldValue
from swagger_client.models.user import User
from swagger_client.models.user_choice_field import UserChoiceField
from swagger_client.models.user_filtering_request import UserFilteringRequest
from swagger_client.models.user_group import UserGroup
from swagger_client.models.user_group_reference import UserGroupReference
from swagger_client.models.user_reference import UserReference
from swagger_client.models.user_reference_search_result import UserReferenceSearchResult
from swagger_client.models.user_search_result import UserSearchResult
from swagger_client.models.wiki_outline_search_result import WikiOutlineSearchResult
from swagger_client.models.wiki_page import WikiPage
from swagger_client.models.wiki_page_reference import WikiPageReference
from swagger_client.models.wiki_render_request import WikiRenderRequest
from swagger_client.models.wiki_text_field import WikiTextField
from swagger_client.models.wiki_text_field_multi_value import WikiTextFieldMultiValue
from swagger_client.models.wiki_text_field_value import WikiTextFieldValue
from swagger_client.models.workflow_transition import WorkflowTransition
from swagger_client.models.working_set_information import WorkingSetInformation
from swagger_client.models.working_set_item_mapping import WorkingSetItemMapping
from swagger_client.models.working_set_items_mapping_request import WorkingSetItemsMappingRequest
from swagger_client.models.working_set_minimal import WorkingSetMinimal
from swagger_client.models.working_set_permission_request import WorkingSetPermissionRequest
from swagger_client.models.working_set_reference import WorkingSetReference
from swagger_client.models.working_set_tracker import WorkingSetTracker
from swagger_client.models.working_set_tracker_update_request import WorkingSetTrackerUpdateRequest
from swagger_client.models.working_set_update_request import WorkingSetUpdateRequest
