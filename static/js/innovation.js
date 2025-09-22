// Innovation features JavaScript

class InnovationFeatures {
    constructor() {
        this.initializeEventListeners();
        this.initializeTabs();
    }

    initializeTabs() {
        const tabBtns = document.querySelectorAll('.tab-btn');
        const tabContents = document.querySelectorAll('.tab-content');

        tabBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                const targetTab = btn.dataset.tab;
                
                // Remove active class from all tabs and contents
                tabBtns.forEach(b => b.classList.remove('active'));
                tabContents.forEach(c => c.classList.remove('active'));
                
                // Add active class to clicked tab and corresponding content
                btn.classList.add('active');
                document.getElementById(targetTab + '-tab').classList.add('active');
            });
        });
    }

    initializeEventListeners() {
        // Enhanced paper generation
        const enhancedBtn = document.getElementById('generate-enhanced');
        if (enhancedBtn) {
            enhancedBtn.addEventListener('click', () => this.generateEnhancedPaper());
        }

        // Quality analysis
        const analyzeBtn = document.getElementById('analyze-quality');
        if (analyzeBtn) {
            analyzeBtn.addEventListener('click', () => this.analyzeQuality());
        }

        // Research proposal
        const proposalBtn = document.getElementById('generate-proposal');
        if (proposalBtn) {
            proposalBtn.addEventListener('click', () => this.generateProposal());
        }

        // Research gaps
        const gapsBtn = document.getElementById('find-gaps');
        if (gapsBtn) {
            gapsBtn.addEventListener('click', () => this.findResearchGaps());
        }

        // Counterarguments
        const counterBtn = document.getElementById('generate-counter');
        if (counterBtn) {
            counterBtn.addEventListener('click', () => this.generateCounterarguments());
        }
    }

    async generateEnhancedPaper() {
        const topic = document.getElementById('enhanced-topic').value;
        const paperType = document.getElementById('enhanced-type').value;
        const length = document.getElementById('enhanced-length').value;

        if (!topic) {
            alert('Please enter a topic');
            return;
        }

        this.showLoading('Generating enhanced paper...');

        try {
            const response = await fetch('/api/innovation/enhanced-paper', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    topic: topic,
                    paper_type: paperType,
                    length: length
                })
            });

            const result = await response.json();

            if (result.success) {
                this.displayEnhancedResults(result);
            } else {
                alert('Error: ' + result.error);
            }
        } catch (error) {
            alert('Error generating enhanced paper: ' + error.message);
        } finally {
            this.hideLoading();
        }
    }

    async analyzeQuality() {
        const content = document.getElementById('analysis-content').value;

        if (!content) {
            alert('Please enter paper content to analyze');
            return;
        }

        this.showLoading('Analyzing paper quality...');

        try {
            const response = await fetch('/api/innovation/analyze-quality', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    content: content
                })
            });

            const result = await response.json();

            if (result.success) {
                this.displayQualityAnalysis(result);
            } else {
                alert('Error: ' + result.error);
            }
        } catch (error) {
            alert('Error analyzing quality: ' + error.message);
        } finally {
            this.hideLoading();
        }
    }

    async generateProposal() {
        const researchIdea = document.getElementById('research-idea').value;
        const fundingType = document.getElementById('funding-type').value;

        if (!researchIdea) {
            alert('Please enter a research idea');
            return;
        }

        this.showLoading('Generating research proposal...');

        try {
            const response = await fetch('/api/innovation/research-proposal', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    research_idea: researchIdea,
                    funding_type: fundingType
                })
            });

            const result = await response.json();

            if (result.success) {
                this.displayProposalResults(result);
            } else {
                alert('Error: ' + result.error);
            }
        } catch (error) {
            alert('Error generating proposal: ' + error.message);
        } finally {
            this.hideLoading();
        }
    }

    displayEnhancedResults(result) {
        const resultsDiv = document.getElementById('enhanced-results');
        if (!resultsDiv) return;

        resultsDiv.innerHTML = `
            <div class="enhanced-paper-results">
                <h3>✨ Enhanced Paper Generated</h3>
                
                <div class="quality-score">
                    <h4>Quality Score: ${result.quality_score.grade} (${result.quality_score.overall_score}%)</h4>
                </div>

                <div class="content-section">
                    <h4>📄 Paper Content</h4>
                    <div style="max-height: 300px; overflow-y: auto; white-space: pre-wrap;">${result.paper.content}</div>
                </div>

                <div class="metric-grid">
                    <div class="metric-card">
                        <h5>🔍 Research Gaps</h5>
                        <div style="max-height: 200px; overflow-y: auto;">${result.research_gaps.replace(/\n/g, '<br>')}</div>
                    </div>
                    <div class="metric-card">
                        <h5>🔬 Methodology</h5>
                        <div style="max-height: 200px; overflow-y: auto;">${result.methodology_suggestions.replace(/\n/g, '<br>')}</div>
                    </div>
                    <div class="metric-card">
                        <h5>📈 Impact Assessment</h5>
                        <div style="max-height: 200px; overflow-y: auto;">${result.impact_assessment.replace(/\n/g, '<br>')}</div>
                    </div>
                </div>

                <div class="suggestions-list">
                    <h4>💡 Improvement Suggestions</h4>
                    <ul>
                        ${result.improvement_suggestions.map(s => `<li>${s}</li>`).join('')}
                    </ul>
                </div>
            </div>
        `;
        resultsDiv.style.display = 'block';
    }

    displayQualityAnalysis(result) {
        const analysisDiv = document.getElementById('quality-results');
        if (!analysisDiv) return;

        analysisDiv.innerHTML = `
            <div class="quality-analysis-results">
                <h3>📊 Paper Quality Analysis</h3>
                
                <div class="quality-score">
                    <h4>Overall Grade: ${result.quality_score.grade} (${result.quality_score.overall_score}%)</h4>
                </div>

                <div class="metric-grid">
                    <div class="metric-card">
                        <h5>📖 Readability Analysis</h5>
                        <p><strong>Word Count:</strong> ${result.readability.word_count}</p>
                        <p><strong>Avg Words/Sentence:</strong> ${result.readability.avg_words_per_sentence}</p>
                        <p><strong>Reading Level:</strong> ${result.readability.readability_level}</p>
                        <p><strong>Academic Score:</strong> ${result.readability.academic_score}</p>
                    </div>

                    <div class="metric-card">
                        <h5>🎯 Argument Structure</h5>
                        <p><strong>Claims:</strong> ${result.argument_structure.claim_density}</p>
                        <p><strong>Evidence:</strong> ${result.argument_structure.evidence_density}</p>
                        <p><strong>Balance:</strong> ${result.argument_structure.argument_balance}</p>
                        <p><strong>Flow Score:</strong> ${result.argument_structure.flow_score}</p>
                    </div>
                </div>

                <div class="suggestions-list">
                    <h4>💡 Improvement Suggestions</h4>
                    <ul>
                        ${result.suggestions.map(s => `<li>${s}</li>`).join('')}
                    </ul>
                </div>
            </div>
        `;
        analysisDiv.style.display = 'block';
    }

    displayProposalResults(result) {
        const proposalDiv = document.getElementById('proposal-results');
        if (!proposalDiv) return;

        proposalDiv.innerHTML = `
            <div class="proposal-results">
                <h3>📋 Research Proposal Generated</h3>
                
                <div class="metric-grid">
                    <div class="metric-card">
                        <h5>📝 Proposal Outline</h5>
                        <div style="max-height: 300px; overflow-y: auto;">${result.proposal_outline.replace(/\n/g, '<br>')}</div>
                    </div>
                    <div class="metric-card">
                        <h5>🔬 Methodology</h5>
                        <div style="max-height: 300px; overflow-y: auto;">${result.methodology.replace(/\n/g, '<br>')}</div>
                    </div>
                    <div class="metric-card">
                        <h5>📈 Impact Assessment</h5>
                        <div style="max-height: 300px; overflow-y: auto;">${result.impact_assessment.replace(/\n/g, '<br>')}</div>
                    </div>
                </div>
            </div>
        `;
        proposalDiv.style.display = 'block';
    }

    async findResearchGaps() {
        const topic = document.getElementById('gaps-topic').value;
        if (!topic) {
            alert('Please enter a research topic');
            return;
        }

        this.showLoading('Finding research gaps...');

        try {
            // Using innovation service directly
            const response = await fetch('/api/innovation/research-gaps', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ topic: topic })
            });

            const result = await response.json();

            if (result.success) {
                this.displayGapsResults(result.research_gaps);
            } else {
                alert('Error: ' + result.error);
            }
        } catch (error) {
            alert('Error finding research gaps: ' + error.message);
        } finally {
            this.hideLoading();
        }
    }

    async generateCounterarguments() {
        const mainArgument = document.getElementById('counter-argument').value;
        const topic = document.getElementById('counter-topic').value;

        if (!mainArgument || !topic) {
            alert('Please enter both argument and topic');
            return;
        }

        this.showLoading('Generating counterarguments...');

        try {
            const response = await fetch('/api/innovation/counterarguments', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    main_argument: mainArgument,
                    topic: topic
                })
            });

            const result = await response.json();

            if (result.success) {
                this.displayCounterResults(result.counterarguments);
            } else {
                alert('Error: ' + result.error);
            }
        } catch (error) {
            alert('Error generating counterarguments: ' + error.message);
        } finally {
            this.hideLoading();
        }
    }

    displayGapsResults(gaps) {
        const resultsDiv = document.getElementById('gaps-results');
        if (!resultsDiv) return;

        resultsDiv.innerHTML = `
            <div class="gaps-results">
                <h3>🔍 Research Gaps Analysis</h3>
                <div class="content-section">
                    <div style="white-space: pre-wrap;">${gaps}</div>
                </div>
            </div>
        `;
        resultsDiv.style.display = 'block';
    }

    displayCounterResults(counterarguments) {
        const resultsDiv = document.getElementById('gaps-results');
        if (!resultsDiv) return;

        const existingContent = resultsDiv.innerHTML;
        resultsDiv.innerHTML = existingContent + `
            <div class="counter-results" style="margin-top: 20px;">
                <h3>⚖️ Counterarguments Analysis</h3>
                <div class="content-section">
                    <div style="white-space: pre-wrap;">${counterarguments}</div>
                </div>
            </div>
        `;
        resultsDiv.style.display = 'block';
    }

    showLoading(message) {
        const loadingDiv = document.getElementById('loading');
        if (loadingDiv) {
            loadingDiv.innerHTML = `<p>${message}</p>`;
            loadingDiv.style.display = 'block';
        }
    }

    hideLoading() {
        const loadingDiv = document.getElementById('loading');
        if (loadingDiv) {
            loadingDiv.style.display = 'none';
        }
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
    new InnovationFeatures();
});