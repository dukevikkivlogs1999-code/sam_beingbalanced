#!/usr/bin/env python3
"""
Navigation Updater for Being Balanced Website

This script updates the navigation structure across all HTML files in the project.
It replaces the existing navigation with the new structure including:
- Resources page
- Podcasts page  
- Updated dropdown menus
- Consistent styling for all pages

Usage:
    python update_nav.py
"""

import glob
import os
import re
from pathlib import Path

class NavigationUpdater:
    def __init__(self):
        self.current_dir = Path(__file__).parent
        self.html_files = list(self.current_dir.glob("*.html"))
        
        # New navigation structure
        self.new_navigation = """
        <!-- New Navigation Structure -->
        <nav id="main-nav" class="elementor-nav-menu--main">
            <ul class="elementor-nav-menu">
                <li class="menu-item menu-item-type-post_type menu-item-object-page current-menu-item page_item current_page_item">
                    <a href="index.html" class="elementor-item elementor-item-active">Home</a>
                </li>
                <li class="menu-item menu-item-type-post_type menu-item-object-page">
                    <a href="about-us-being-balanced-consultancy-ventures.html" class="elementor-item">About Us</a>
                </li>
                <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children">
                    <a href="services.html" class="elementor-item">Services</a>
                    <ul class="sub-menu elementor-nav-menu--dropdown">
                        <li class="menu-item menu-item-has-children">
                            <a href="#">For Individuals</a>
                            <ul class="sub-menu">
                                <li><a href="one-on-one-counseling.html">One on One Counseling</a></li>
                                <li><a href="support-groups.html">Support Groups</a></li>
                                <li><a href="group-therapy.html">Group Therapy</a></li>
                                <li><a href="employee-assistance-program.html">Employee Assistance</a></li>
                                <li><a href="training-development.html">Training & Development</a></li>
                            </ul>
                        </li>
                        <li class="menu-item menu-item-has-children">
                            <a href="#">For Institutions/Schools/Colleges</a>
                            <ul class="sub-menu">
                                <li><a href="trainings-workshops.html">Training & Workshops</a></li>
                                <li><a href="internships.html">Internships</a></li>
                                <li><a href="services.html#institutional">Consultancy Services</a></li>
                            </ul>
                        </li>
                        <li class="menu-item menu-item-has-children">
                            <a href="#">For Corporates</a>
                            <ul class="sub-menu">
                                <li><a href="employee-assistance-program.html">EAP Programs</a></li>
                                <li><a href="training-development.html#corporate">Corporate Training</a></li>
                            </ul>
                        </li>
                    </ul>
                </li>
                <li class="menu-item menu-item-type-post_type menu-item-object-page">
                    <a href="our-team.html" class="elementor-item">Our Team</a>
                </li>
                <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children">
                    <a href="#" class="elementor-item">Events & Media</a>
                    <ul class="sub-menu elementor-nav-menu--dropdown">
                        <li><a href="past-events.html">Past Events</a></li>
                        <li><a href="media.html">Media</a></li>
                    </ul>
                </li>
                <li class="menu-item menu-item-type-post_type menu-item-object-page">
                    <a href="resources.html" class="elementor-item">Resources</a>
                </li>
                <li class="menu-item menu-item-type-post_type menu-item-object-page">
                    <a href="podcasts.html" class="elementor-item">Podcasts</a>
                </li>
                <li class="menu-item menu-item-type-post_type menu-item-object-page">
                    <a href="blogs.html" class="elementor-item">Blogs</a>
                </li>
                <li class="menu-item menu-item-type-post_type menu-item-object-page">
                    <a href="contact.html" class="elementor-item">Contact</a>
                </li>
            </ul>
        </nav>
        """

    def find_navigation_blocks(self, content):
        """Find navigation blocks in HTML content"""
        nav_patterns = [
            # Elementor navigation blocks
            r'<nav[^>]*class="[^"]*elementor-nav-menu--main[^"]*"[^>]*>.*?</nav>',
            r'<ul[^>]*class="[^"]*elementor-nav-menu[^"]*"[^>]*>.*?</ul>',
            r'<div[^>]*class="[^"]*elementor-widget-nav-menu[^"]*"[^>]*>.*?</div>',
            r'<div[^>]*id="menu-[^"]*"[^>]*>.*?</div>',
            # Ekit navigation blocks
            r'<nav[^>]*class="[^"]*ekit-wid-con[^"]*"[^>]*>.*?</nav>',
            r'<ul[^>]*class="[^"]*elementskit-navbar-nav[^"]*"[^>]*>.*?</ul>',
            r'<nav[^>]*class="[^"]*elementor-nav-menu[^"]*"[^>]*>.*?</nav>',
        ]
        
        found_navs = []
        for pattern in nav_patterns:
            matches = re.findall(pattern, content, re.DOTALL | re.IGNORECASE)
            found_navs.extend(matches)
        
        return found_navs

    def replace_navigation(self, content):
        """Replace existing navigation with new structure"""
        # Existing navigation patterns to replace
        patterns_to_replace = [
            r'<nav[^>]*class="[^"]*elementor-nav-menu--main[^"]*"[^>]*>.*?</nav>',
            r'<nav[^>]*class="[^"]*elementskit-menu-container[^"]*"[^>]*>.*?</nav>',
            r'<ul[^>]*class="[^"]*elementor-nav-menu[^"]*"[^>]*>.*?</ul>(?=[^<]*<nav|</div>)',
            r'<ul[^>]*class="[^"]*elementskit-navbar-nav[^"]*"[^>]*>.*?</ul>',
        ]
        
        # Add navigation styles and structure
        nav_wrapper = '''
        <!-- Updated Navigation 2025 -->
        <div class="elementor-widget-wrap elementor-element-populated">
            <div class="elementor-element elementor-element-babb0f0 elementor-nav-menu__align-start de_scroll_animation_no elementor-widget elementor-widget-nav-menu" data-e-type="widget" data-element_type="widget" data-id="babb0f0" data-widget_type="nav-menu.default">
                <div class="elementor-widget-container">
                    <nav class="elementor-nav-menu--main elementor-nav-menu__container elementor-nav-menu--layout-horizontal" data-e-nav-menu="square">
                        <ul id="menu-1-babb0f0" class="elementor-nav-menu">
                            <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-home current-menu-item page_item page-item-5279 current_page_item menu-item-5318">
                                <a href="index.html" class="elementor-item elementor-item-active" aria-current="page">Home</a>
                            </li>
                            <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-4828">
                                <a href="about-us-being-balanced-consultancy-ventures.html" class="elementor-item">About</a>
                            </li>
                            <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-has-children menu-item-4657">
                                <a href="services.html" class="elementor-item">Services</a>
                                <ul class="sub-menu elementor-nav-menu--dropdown">
                                    <li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-5328">
                                        <a href="#" class="elementor-item">For Individuals</a>
                                        <ul class="sub-menu elementor-nav-menu--dropdown">
                                            <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-5327">
                                                <a href="one-on-one-counseling.html" class="elementor-sub-item">One on One Counseling</a>
                                            </li>
                                            <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-5326">
                                                <a href="support-groups.html" class="elementor-sub-item">Support Groups</a>
                                            </li>
                                            <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1234">
                                                <a href="group-therapy.html" class="elementor-sub-item">Group Therapy</a>
                                            </li>
                                            <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-5324">
                                                <a href="employee-assistance-program.html" class="elementor-sub-item">Employee Assistance Program</a>
                                            </li>
                                        </ul>
                                    </li>
                                    <li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-5329">
                                        <a href="#" class="elementor-item">For Institutions</a>
                                        <ul class="sub-menu elementor-nav-menu--dropdown">
                                            <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1235">
                                                <a href="trainings-workshops.html" class="elementor-sub-item">Training & Workshops</a>
                                            </li>
                                            <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1236">
                                                <a href="internships.html" class="elementor-sub-item">Internships</a>
                                            </li>
                                        </ul>
                                    </li>
                                    <li class="menu-item menu-item-type-custom menu-item-object-custom menu-item-has-children menu-item-5331">
                                        <a href="#" class="elementor-item">For Corporates</a>
                                        <ul class="sub-menu elementor-nav-menu--dropdown">
                                            <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-5324">
                                                <a href="employee-assistance-program.html#corporate" class="elementor-sub-item">EAP Programs</a>
                                            </li>
                                        </ul>
                                    </li>
                                </ul>
                            </li>
                            <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1237">
                                <a href="our-team.html" class="elementor-item">Our Team</a>
                            </li>
                            <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1238">
                                <a href="resources.html" class="elementor-item">Resources</a>
                            </li>
                            <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1239">
                                <a href="podcasts.html" class="elementor-item">Podcasts</a>
                            </li>
                            <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1240">
                                <a href="blogs.html" class="elementor-item">Blogs</a>
                            </li>
                            <li class="menu-item menu-item-type-post_type menu-item-object-page menu-item-1241">
                                <a href="contact.html" class="elementor-item">Contact</a>
                            </li>
                        </ul>
                    </nav>
                </div>
            </div>
        </div>
        '''
        
        # Replace first occurrence of each navigation pattern
        for pattern in patterns_to_replace:
            content = re.sub(pattern, nav_wrapper, content, count=1, flags=re.DOTALL | re.IGNORECASE)
        
        return content

    def update_file(self, file_path):
        """Update navigation for a single HTML file"""
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            original_content = content
            updated_content = self.replace_navigation(content)
            
            # Only update if changes were made
            if updated_content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(updated_content)
                print(f"✓ Updated: {file_path.name}")
                return True
            else:
                print(f"⚠ No navigation blocks found in: {file_path.name}")
                return False
                
        except Exception as e:
            print(f"✗ Error updating {file_path.name}: {e}")
            return False

    def run_update(self):
        """Run navigation update across all HTML files"""
        print("Starting navigation update...")
        print(f"Found {len(self.html_files)} HTML files to process\n")
        
        updated_count = 0
        errors_count = 0
        
        for file_path in sorted(self.html_files):
            # Skip update_nav.py itself and README if it has .html extension
            if file_path.name in ['update_nav.py', 'README.html']:
                continue
                
            if self.update_file(file_path):
                updated_count += 1
            else:
                errors_count += 1
        
        print(f"\n✓ Navigation update complete!")
        print(f"Updated: {updated_count} files")
        print(f"Errors: {errors_count} files")
        print(f"Total: {len(self.html_files)} files processed")

if __name__ == "__main__":
    updater = NavigationUpdater()
    updater.run_update()
