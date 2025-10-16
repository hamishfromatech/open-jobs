from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user
from datetime import datetime
from models import db, Job
from forms import JobForm

# Create Blueprint for jobs
jobs = Blueprint('jobs', __name__)

@jobs.route('/jobs')
def job_board():
    """Display all active job listings"""
    page = request.args.get('page', 1, type=int)
    jobs = Job.query.filter_by(
        status='active',
        is_deleted=False
    ).order_by(Job.created_at.desc()).paginate(page=page, per_page=10)
    return render_template('jobs/board.html', jobs=jobs)

@jobs.route('/jobs/create', methods=['GET', 'POST'])
@login_required
def create_job():
    """Create a new job listing"""
    if not current_user.is_admin:
        flash('Only administrators can post job listings.', 'error')
        return redirect(url_for('jobs.job_board'))
    
    form = JobForm()
    if form.validate_on_submit():
        job = Job(
            title=form.title.data,
            company=form.company.data,
            location=form.location.data,
            description=form.description.data,
            requirements=form.requirements.data,
            salary_range=form.salary_range.data,
            job_type=form.job_type.data,
            experience_level=form.experience_level.data,
            skills=form.skills.data,
            benefits=form.benefits.data,
            deadline=form.deadline.data,
            user_id=current_user.id
        )
        
        db.session.add(job)
        db.session.commit()
        flash('Job listing created successfully!', 'success')
        return redirect(url_for('jobs.job_board'))
    
    return render_template('jobs/create.html', form=form)

@jobs.route('/jobs/<int:job_id>')
def view_job(job_id):
    """View a specific job listing"""
    job = Job.query.get_or_404(job_id)
    return render_template('jobs/view.html', job=job)

@jobs.route('/jobs/<int:job_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_job(job_id):
    """Edit a job listing"""
    job = Job.query.get_or_404(job_id)
    
    # Ensure only the job creator can edit
    if job.user_id != current_user.id:
        flash('You do not have permission to edit this job listing.', 'error')
        return redirect(url_for('jobs.job_board'))
    
    if request.method == 'POST':
        job.title = request.form.get('title')
        job.company = request.form.get('company')
        job.location = request.form.get('location')
        job.description = request.form.get('description')
        job.requirements = request.form.get('requirements')
        job.salary_range = request.form.get('salary_range')
        job.job_type = request.form.get('job_type')
        job.experience_level = request.form.get('experience_level')
        job.skills = request.form.get('skills')
        job.deadline = datetime.strptime(request.form.get('deadline'), '%Y-%m-%d')
        
        db.session.commit()
        flash('Job listing updated successfully!', 'success')
        return redirect(url_for('jobs.view_job', job_id=job.id))
    
    return render_template('jobs/edit.html', job=job)

@jobs.route('/jobs/<int:job_id>/delete', methods=['POST'])
@login_required
def delete_job(job_id):
    """Delete a job listing"""
    job = Job.query.get_or_404(job_id)
    
    # Ensure only the job creator can delete
    if job.user_id != current_user.id:
        flash('You do not have permission to delete this job listing.', 'error')
        return redirect(url_for('jobs.job_board'))
    
    db.session.delete(job)
    db.session.commit()
    flash('Job listing deleted successfully!', 'success')
    return redirect(url_for('jobs.job_board'))

@jobs.route('/jobs/search')
def search_jobs():
    """Search for jobs based on various criteria"""
    query = request.args.get('q', '')
    location = request.args.get('location', '')
    job_type = request.args.get('type', '')
    experience = request.args.get('experience', '')
    
    jobs_query = Job.query.filter_by(status='active')
    
    if query:
        jobs_query = jobs_query.filter(
            db.or_(
                Job.title.ilike(f'%{query}%'),
                Job.company.ilike(f'%{query}%'),
                Job.description.ilike(f'%{query}%'),
                Job.skills.ilike(f'%{query}%')
            )
        )
    
    if location:
        jobs_query = jobs_query.filter(Job.location.ilike(f'%{location}%'))
    
    if job_type:
        jobs_query = jobs_query.filter(Job.job_type == job_type)
    
    if experience:
        jobs_query = jobs_query.filter(Job.experience_level == experience)
    
    page = request.args.get('page', 1, type=int)
    jobs = jobs_query.order_by(Job.created_at.desc()).paginate(page=page, per_page=10)
    
    return render_template('jobs/search.html', jobs=jobs, query=query, location=location,
                         job_type=job_type, experience=experience)
