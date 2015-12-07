from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^create-user', views.create_user, name='create_user'),
    url(r'^thanks', views.thanks, name='thanks'),
    url(r'^$', views.index, name='index'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^profile', views.user_profile, name='user_profile'),
    url(r'^logout', views.logout_view, name='logout_view'),
    url(r'^add-education/', views.create_education, name='create_education'),
    url(r'^edit-education/(?P<education_id>[0-9]+)', views.edit_education, name='edit_education'),
    url(r'^edit-education/', views.edit_education, name='edit_education'),
    url(r'^edit-skill/(?P<skill_id>[0-9]+)', views.edit_skill, name='edit_skill'),
    url(r'^edit-skill', views.edit_skill, name='edit_skill'),
    url(r'^remove-skill/(?P<skill_id>[0-9]+)', views.remove_skill, name='remove_skill'),
    url(r'^remove-experience/(?P<experience_id>[0-9]+)', views.remove_experience, name='remove_experience'),
    url(r'^remove-education/(?P<education_id>[0-9]+)', views.remove_education, name='remove_education'),
    url(r'^add-education-bp/(?P<item_id>[0-9]+)', views.add_education_bp, name='add_education_bp'),
    url(r'^add-education-bp', views.add_education_bp, name='add_education_bp'),
    url(r'^add-skill-bp/(?P<item_id>[0-9]+)', views.add_skill_bp, name='add_skill_bp'),
    url(r'^add-skill-bp', views.add_skill_bp, name='add_skill_bp'),
    url(r'^add-experience-bp/(?P<item_id>[0-9]+)', views.add_experience_bp, name='add_experience_bp'),
    url(r'^add-experience-bp', views.add_experience_bp, name='add_experience_bp'),
    url(r'^add-award-bp/(?P<item_id>[0-9]+)', views.add_award_bp, name='add_award_bp'),
    url(r'^add-award-bp', views.add_award_bp, name='add_award_bp'),
    url(r'^review-comments', views.review_comments, name='review_comments'),
    url(r'^view-my-resume', views.view_my_resume, name='view_my_resume'),
    url(r'^generate-pdf', views.generate_pdf, name='generate_pdf'),
    url(r'^choose-resume-to-edit', views.choose_resume_to_edit, name='choose_resume_to_edit'),
    url(r'^search-resume-results', views.search_resume_results, name='search_resume_results'),
    url(r'^comment-resume', views.comment_resume, name='comment_resume'),
    url(r'^add-experience/', views.create_experience, name='create_experience'),
    url(r'^edit-experience/(?P<experience_id>[0-9]+)', views.edit_experience, name='edit_experience'),
    url(r'^edit-experience/', views.edit_experience, name='edit_experience'),
    url(r'^add-award', views.create_award, name='create_award'),
    url(r'^edit-award/(?P<award_id>[0-9]+)', views.edit_award, name='edit_award'),
    url(r'^edit-award/', views.edit_award, name='edit_award'),
    url(r'^remove-award/(?P<award_id>[0-9]+)', views.remove_award, name='remove_award'),
    url(r'^add-skill-category', views.create_skill_category, name='create_skill_category'),
    url(r'^remove-bp/(?P<bp_id>[0-9]+)', views.remove_bp, name='remove_bp'),
    url(r'^move-up-bp/(?P<bp_id>[0-9]+)', views.move_up_bp, name='move_up_bp'),
    url(r'^move-down-bp/(?P<bp_id>[0-9]+)', views.move_down_bp, name='move_down_bp'),
    url(r'^move-up-education/(?P<education_id>[0-9]+)', views.move_up_education, name='move_up_education'),
    url(r'^move-down-education/(?P<education_id>[0-9]+)', views.move_down_education, name='move_down_education'),
    url(r'^move-up-award/(?P<award_id>[0-9]+)', views.move_up_award, name='move_up_award'),
    url(r'^move-down-award/(?P<award_id>[0-9]+)', views.move_down_award, name='move_down_award'),
    url(r'^move-up-skill/(?P<object_id>[0-9]+)', views.move_up_skill, name='move_up_skill'),
    url(r'^move-down-skill/(?P<object_id>[0-9]+)', views.move_down_skill, name='move_down_skill'),
    url(r'^move-up-experience/(?P<object_id>[0-9]+)', views.move_up_experience, name='move_up_experience'),
    url(r'^move-down-experience/(?P<object_id>[0-9]+)', views.move_down_experience, name='move_down_experience'),
    url(r'^move-up-section/(?P<section_name>\w+)', views.move_up_section, name='move_up_section'),
    url(r'^move-down-section/(?P<section_name>\w+)', views.move_down_section, name='move_down_section'),
    url(r'^enable-bp/(?P<bp_id>[0-9]+)', views.enable_bp, name='enable_bp'),
    url(r'^disable-bp/(?P<bp_id>[0-9]+)', views.disable_bp, name='disable_bp'),
    url(r'^enable-education/(?P<bp_id>[0-9]+)', views.enable_education, name='enable_education'),
    url(r'^disable-education/(?P<bp_id>[0-9]+)', views.disable_education, name='disable_education'),
    url(r'^enable-experience/(?P<bp_id>[0-9]+)', views.enable_experience, name='enable_experience'),
    url(r'^disable-experience/(?P<bp_id>[0-9]+)', views.disable_experience, name='disable_experience'),
    url(r'^enable-skill/(?P<bp_id>[0-9]+)', views.enable_skill, name='enable_skill'),
    url(r'^disable-skill/(?P<bp_id>[0-9]+)', views.disable_skill, name='disable_skill'),
    url(r'^enable-award/(?P<bp_id>[0-9]+)', views.enable_award, name='enable_award'),
    url(r'^disable-award/(?P<bp_id>[0-9]+)', views.disable_award, name='disable_award'),
    url(r'^add-bp-comment/(?P<bp_id>[0-9]+)', views.add_bp_comment, name='add_bp_comment'),
    url(r'^get-comments-for-bp/(?P<bp_id>[0-9]+)', views.get_comments_for_bp, name='get_comments_for_bp'),
    url(r'^upvote-comment/(?P<comment_id>[0-9]+)', views.upvote_comment, name='upvote_comment'),
    url(r'^downvote-comment/(?P<comment_id>[0-9]+)', views.downvote_comment, name='downvote_comment'),
]