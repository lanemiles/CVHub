from django.conf.urls import url
from . import views

urlpatterns = [
    # PROFILE
    url(r'^create-user', views.create_user, name='create_user'),
    url(r'^$', views.user_profile, name='user_profile'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^profile', views.user_profile, name='user_profile'),
    url(r'^logout', views.logout_view, name='logout_view'),
    url(r'^edit-information/', views.edit_information, name='edit_information'),

    # EDUCATION
    url(r'^add-education/', views.create_education, name='create_education'),
    url(r'^edit-education/(?P<education_id>[0-9]+)', views.edit_education, name='edit_education'),
    url(r'^edit-education/', views.edit_education, name='edit_education'),
    url(r'^remove-education/(?P<education_id>[0-9]+)', views.remove_education, name='remove_education'),
    url(r'^add-education-bp/(?P<item_id>[0-9]+)', views.add_education_bp, name='add_education_bp'),
    url(r'^add-education-bp', views.add_education_bp, name='add_education_bp'),
    url(r'^move-up-education/(?P<education_id>[0-9]+)', views.move_up_education, name='move_up_education'),
    url(r'^move-down-education/(?P<education_id>[0-9]+)', views.move_down_education, name='move_down_education'),
    url(r'^enable-education/(?P<education_id>[0-9]+)', views.enable_education, name='enable_education'),
    url(r'^disable-education/(?P<education_id>[0-9]+)', views.disable_education, name='disable_education'),
    url(r'^add-education-comment/(?P<education_id>[0-9]+)', views.add_education_comment, name='add_education_comment'),
    url(r'^get-comments-for-education/(?P<education_id>[0-9]+)', views.get_comments_for_education, name='get_comments_for_education'),

    # EXPERIENCE
    url(r'^add-experience/', views.create_experience, name='create_experience'),
    url(r'^edit-experience/(?P<experience_id>[0-9]+)', views.edit_experience, name='edit_experience'),
    url(r'^edit-experience/', views.edit_experience, name='edit_experience'),
    url(r'^add-experience-bp/(?P<item_id>[0-9]+)', views.add_experience_bp, name='add_experience_bp'),
    url(r'^add-experience-bp', views.add_experience_bp, name='add_experience_bp'),
    url(r'^enable-experience/(?P<experience_id>[0-9]+)', views.enable_experience, name='enable_experience'),
    url(r'^disable-experience/(?P<experience_id>[0-9]+)', views.disable_experience, name='disable_experience'),
    url(r'^add-experience-comment/(?P<experience_id>[0-9]+)', views.add_experience_comment, name='add_experience_comment'),
    url(r'^get-comments-for-experience/(?P<experience_id>[0-9]+)', views.get_comments_for_experience, name='get_comments_for_experience'),
    url(r'^move-up-experience/(?P<experience_id>[0-9]+)', views.move_up_experience, name='move_up_experience'),
    url(r'^move-down-experience/(?P<experience_id>[0-9]+)', views.move_down_experience, name='move_down_experience'),
    url(r'^remove-experience/(?P<experience_id>[0-9]+)', views.remove_experience, name='remove_experience'),

    # SKILL
    url(r'^add-skill-category', views.create_skill_category, name='create_skill_category'),
    url(r'^add-skill-bp/(?P<item_id>[0-9]+)', views.add_skill_bp, name='add_skill_bp'),
    url(r'^add-skill-bp', views.add_skill_bp, name='add_skill_bp'),
    url(r'^move-up-skill/(?P<skill_id>[0-9]+)', views.move_up_skill, name='move_up_skill'),
    url(r'^move-down-skill/(?P<skill_id>[0-9]+)', views.move_down_skill, name='move_down_skill'),
    url(r'^add-skill-comment/(?P<skill_id>[0-9]+)', views.add_skill_comment, name='add_skill_comment'),
    url(r'^get-comments-for-skill/(?P<skill_id>[0-9]+)', views.get_comments_for_skill, name='get_comments_for_skill'),
    url(r'^enable-skill/(?P<skill_id>[0-9]+)', views.enable_skill, name='enable_skill'),
    url(r'^disable-skill/(?P<skill_id>[0-9]+)', views.disable_skill, name='disable_skill'),
    url(r'^edit-skill/(?P<skill_id>[0-9]+)', views.edit_skill, name='edit_skill'),
    url(r'^edit-skill', views.edit_skill, name='edit_skill'),
    url(r'^remove-skill/(?P<skill_id>[0-9]+)', views.remove_skill, name='remove_skill'),

    # AWARD
    url(r'^add-award/', views.create_award, name='create_award'),
    url(r'^edit-award/(?P<award_id>[0-9]+)', views.edit_award, name='edit_award'),
    url(r'^edit-award/', views.edit_award, name='edit_award'),
    url(r'^remove-award/(?P<award_id>[0-9]+)', views.remove_award, name='remove_award'),
    url(r'^add-award-bp/(?P<item_id>[0-9]+)', views.add_award_bp, name='add_award_bp'),
    url(r'^add-award-bp', views.add_award_bp, name='add_award_bp'),
    url(r'^move-up-award/(?P<award_id>[0-9]+)', views.move_up_award, name='move_up_award'),
    url(r'^move-down-award/(?P<award_id>[0-9]+)', views.move_down_award, name='move_down_award'),
    url(r'^add-award-comment/(?P<award_id>[0-9]+)', views.add_award_comment, name='add_award_comment'),
    url(r'^get-comments-for-award/(?P<award_id>[0-9]+)', views.get_comments_for_award, name='get_comments_for_award'),
    url(r'^enable-award/(?P<award_id>[0-9]+)', views.enable_award, name='enable_award'),
    url(r'^disable-award/(?P<award_id>[0-9]+)', views.disable_award, name='disable_award'),


    # BULLET POINT
    url(r'^remove-bp/(?P<bp_id>[0-9]+)', views.remove_bp, name='remove_bp'),
    url(r'^move-up-bp/(?P<bp_id>[0-9]+)', views.move_up_bp, name='move_up_bp'),
    url(r'^move-down-bp/(?P<bp_id>[0-9]+)', views.move_down_bp, name='move_down_bp'),
    url(r'^enable-bp/(?P<bp_id>[0-9]+)', views.enable_bp, name='enable_bp'),
    url(r'^disable-bp/(?P<bp_id>[0-9]+)', views.disable_bp, name='disable_bp'),
    url(r'^add-bp-comment/(?P<bp_id>[0-9]+)', views.add_bp_comment, name='add_bp_comment'),
    url(r'^get-comments-for-bp/(?P<bp_id>[0-9]+)', views.get_comments_for_bp, name='get_comments_for_bp'),

    # COMMENT
    url(r'^review-comments', views.review_comments, name='review_comments'),
    url(r'^accept-comment/(?P<comment_id>[0-9]+)', views.accept_comment, name='accept_comment'),
    url(r'^reject-comment/(?P<comment_id>[0-9]+)', views.reject_comment, name='reject_comment'),
    url(r'^comment-resume', views.comment_resume, name='comment_resume'),
    url(r'^upvote-comment/(?P<comment_id>[0-9]+)', views.upvote_comment, name='upvote_comment'),
    url(r'^downvote-comment/(?P<comment_id>[0-9]+)', views.downvote_comment, name='downvote_comment'),

    # SECTION
    url(r'^accept-section-comment/(?P<section_comment_id>[0-9]+)', views.accept_section_comment, name='accept_section_comment'),
    url(r'^reject-section-comment/(?P<section_comment_id>[0-9]+)', views.reject_section_comment, name='reject_section_comment'),
    url(r'^move-up-section/(?P<section_name>\w+)', views.move_up_section, name='move_up_section'),
    url(r'^move-down-section/(?P<section_name>\w+)', views.move_down_section, name='move_down_section'),
    url(r'^enable-section/(?P<section_name>\w+)', views.enable_section, name='enable_section'),
    url(r'^disable-section/(?P<section_name>\w+)', views.disable_section, name='disable_section'),
    url(r'^get-comments-for-section/(?P<section_name>\w+)/(?P<user_info_id>[0-9]+)', views.get_comments_for_section, name='get_comments_for_section'),
    url(r'^add-section-comment/(?P<section_name>\w+)/(?P<user_info_id>[0-9]+)', views.add_section_comment, name='add_section_comment'),
    url(r'^upvote-section-comment/(?P<section_comment_id>[0-9]+)', views.upvote_section_comment, name='upvote_section_comment'),
    url(r'^downvote-section-comment/(?P<section_comment_id>[0-9]+)', views.downvote_section_comment, name='downvote_section_comment'),

    # PDF
    url(r'^embed-pdf', views.embed_pdf, name='embed_pdf'),
    url(r'^generate-pdf', views.generate_pdf, name='generate_pdf'),
    url(r'^view-pdf', views.view_pdf, name='view_pdf'),

    # SEARCH/EXPLORE
    url(r'^choose-resume-to-edit', views.choose_resume_to_edit, name='choose_resume_to_edit'),
    url(r'^search-resume-results', views.search_resume_results, name='search_resume_results'),
    url(r'^mrc-resumes', views.most_recently_commented_resumes, name='mrc_resumes'),
    url(r'^mp-resumes', views.most_popular_resumes, name='most_popular_resumes'),
    url(r'^random-resume', views.random_resume, name='random_resume'),

    # VIEW RESUME
    url(r'^view-my-resume', views.view_my_resume, name='view_my_resume'),
    url(r'^view-user-resume/(?P<user_id>[0-9]+)', views.view_user_resume, name='view_user_resume'),
    url(r'^resume/(?P<custom_string>\w+)/', views.public_resume_pdf, name='public_resume_pdf'),
]
