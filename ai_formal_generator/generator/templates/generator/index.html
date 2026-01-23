<!DOCTYPE html>
<html>
<head>
    <title>AI Formal Document Generator</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet">

    <script>
        function toggleOther(selectId, inputId) {
            const select = document.getElementById(selectId);
            const input = document.getElementById(inputId);
            input.style.display = select.value === "Other" ? "block" : "none";
        }
    </script>
</head>

<body class="bg-light">
<div class="container mt-5">

    <!-- FORM CARD -->
    <div class="card p-4 shadow">
        <h3 class="text-center mb-3">AI Formal Document Generator</h3>

        <form method="POST" action="{% url 'generate_document' %}">
            {% csrf_token %}

            <!-- Language -->
            <label class="fw-bold">Language</label>
            <select class="form-select mb-3" name="language">
                <option value="English">English</option>
                <option value="Hindi">Hindi</option>
            </select>

            <!-- From Position -->
            <label class="fw-bold">From Position</label>
            <select class="form-select mb-2" id="from_position" name="from_position"
                    onchange="toggleOther('from_position','from_other')">
                {% for pos in positions %}
                <option value="{{ pos }}">{{ pos }}</option>
                {% endfor %}
            </select>
            <input class="form-control mb-3" id="from_other" name="from_other"
                   placeholder="Enter other designation" style="display:none;">

            <!-- To Position -->
            <label class="fw-bold">To Position</label>
            <select class="form-select mb-2" id="to_position" name="to_position"
                    onchange="toggleOther('to_position','to_other')">
                {% for pos in positions %}
                <option value="{{ pos }}">{{ pos }}</option>
                {% endfor %}
            </select>
            <input class="form-control mb-3" id="to_other" name="to_other"
                   placeholder="Enter other designation" style="display:none;">

            <!-- Date -->
            <label class="fw-bold">Office Order Date</label>
            <input type="date" class="form-control mb-3" name="order_date">

            <!-- Reference -->
            <label class="fw-bold">Reference ID</label>
            <input class="form-control mb-3" name="reference_id"
                   value="BISAG-N/Office Order/2026/">

            <!-- Prompt -->
            <label class="fw-bold">Document Instruction</label>
            <textarea class="form-control mb-3" name="content"
                      placeholder="Write instruction for document generation"
                      rows="4" required></textarea>

            <button class="btn btn-primary w-100">Generate Document</button>
        </form>
    </div>

    <!-- PREVIEW + DOWNLOAD -->
    {% if generated_text %}
    <div class="card mt-4 p-4 shadow">
        <h5 class="fw-bold">Generated Document Preview</h5>

        <pre style="white-space: pre-wrap;">{{ generated_text }}</pre>

        <div class="mt-3">
            <a href="{% url 'download_pdf' %}" class="btn btn-success me-2">
                Download PDF
            </a>

            <a href="{% url 'download_docx' %}" class="btn btn-primary">
                Download DOCX
            </a>
        </div>
    </div>
    {% endif %}

</div>
</body>
</html>
