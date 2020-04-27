import sys
import time

new_brand_ids = [4134913]
old_job_ids = [1123989
,1124000
,1124024
,1124027
,1124029
,1124031
,1124034
,1124036
,1138537
,1138545
,1138559]
for new_brand_id in new_brand_ids:
    filename = "execution" + "_" + time.strftime("%Y-%m-%d") + ".sql"

    file = open(filename, "a")

    file.write("\n\nSET @TO_BRAND_ID = " + str(new_brand_id) + ";")

    for old_job_id in old_job_ids:
        file.write("-- Old Job: " + str(old_job_id) + "\n\nSET @OLD_JOB_ID = " + str(
            old_job_id) + ";\n\nINSERT into `job` (title, experience_from, experience_to, description, request_video, third_party_tracking, post_date, position_id, type_id, user_id, template_id, post_immediately, publish_date, start_date, end_date, alias_position, ams_sort_by, language, estimated_start_date, start_immediately, is_matching_template, is_job_details_completed, ats_email_template, job_application_type, work_eligibility_group_id, _enabled, created, updated, deleted, deleted_on, deleted_by, on_boarding_status, brand_id ) SELECT title, experience_from, experience_to, description, request_video, third_party_tracking, post_date, position_id, type_id, user_id, template_id, post_immediately, publish_date, start_date, end_date, alias_position, ams_sort_by, language, estimated_start_date, start_immediately, is_matching_template, is_job_details_completed, ats_email_template, job_application_type, work_eligibility_group_id, _enabled, NOW(), NOW(), deleted, deleted_on, deleted_by, on_boarding_status, @TO_BRAND_ID FROM job WHERE id = @OLD_JOB_ID;\n\nSET @NEW_JOB_ID = LAST_INSERT_ID();\n\nINSERT into `job_compensation` (`job_id`, `compensation_from`, `compensation_to`, `plus_tips`, `plus_commission`, `compensation_rate_id`, `compensation_id`, `_enabled`, `created`, `updated`, `deleted`, `deleted_on`, `deleted_by` ) SELECT @NEW_JOB_ID, `compensation_from`, `compensation_to`, `plus_tips`, `plus_commission`, `compensation_rate_id`, `compensation_id`, `_enabled`, NOW(), NOW(), `deleted`, `deleted_on`, `deleted_by` FROM `job_compensation` WHERE job_id = @OLD_JOB_ID and deleted = 0;\nINSERT into `job_skill` (`job_id`, `skill_id`, `must_have` ) SELECT @NEW_JOB_ID, `skill_id`, `must_have` FROM `job_skill` WHERE job_id = @OLD_JOB_ID;\nINSERT into `job_timing` (`job_id`, `timing_id` ) SELECT @NEW_JOB_ID, `timing_id` FROM `job_timing` WHERE job_id = @OLD_JOB_ID;\nINSERT into `job_application_option` (`job_id`, `application_option_id`, `is_optional`, `_enabled`, `created`, `updated`, `deleted`, `deleted_on`, `deleted_by`) SELECT @NEW_JOB_ID, `application_option_id`, `is_optional`, `_enabled`, NOW(), NOW(), `deleted`, `deleted_on`, `deleted_by` FROM `job_application_option` WHERE job_id = @OLD_JOB_ID and deleted = 0;\nINSERT INTO `job_setting` (`job_id`, `min_life_time`, `max_life_time`, `interview_recession_period`, `interview_window`, `interview_slot`, `public_on`, `switch_date`, `switch_mode`, `number_of_hires`, `evergreen_allowed`, `custom_period_allowed`, `_enabled`, `created`, `updated`, `deleted`, `deleted_on`, `deleted_by`)SELECT @NEW_JOB_ID, `min_life_time`, `max_life_time`, `interview_recession_period`, `interview_window`, `interview_slot`, `public_on`, `switch_date`, `switch_mode`,`number_of_hires`, `evergreen_allowed`, `custom_period_allowed`, `_enabled`, NOW(), NOW(), `deleted`, `deleted_on`, `deleted_by` FROM `job_setting` WHERE job_id = @OLD_JOB_ID and deleted = 0;")

    file.close() ;