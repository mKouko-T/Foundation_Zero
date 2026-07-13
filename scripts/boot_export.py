import os
import datetime

def compile_boot_context():
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    output_file = os.path.join(root_dir, 'BOOT_CONTEXT.md')
    
    files_to_compile = [
        "FZ_VERSION.md",
        "README.md",
        "REPOSITORY_CONSTITUTION.md",
        ".foundation_zero/ENGINEERING_DOCTRINE.md",
        "docs/playbooks/templates/BOOTSTRAP_TEMPLATE.md",
        "docs/protocols/Protocol_Repository_Certification.md",
        "docs/governance/PROPOSAL_TEMPLATE.md"
    ]
    
    compiled_content = []
    compiled_content.append("# Foundation Zero: Compiled Boot Context\n")
    compiled_content.append(f"**Generated:** {datetime.datetime.utcnow().isoformat()}Z\n")
    compiled_content.append("**Purpose:** This is a derived build artifact containing the complete 'Foundation Zero Lite' core. It exists solely to allow downstream AI orchestrators (like ChatGPT) to ingest the entire compiler state in a single file fetch.\n\n")
    compiled_content.append("---\n\n")
    
    for relative_path in files_to_compile:
        file_path = os.path.join(root_dir, relative_path)
        if os.path.exists(file_path):
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            compiled_content.append(f"## FILE: `{relative_path}`\n\n```markdown\n{content}\n```\n\n---\n\n")
        else:
            print(f"Warning: Could not find {relative_path}")
            
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("".join(compiled_content))
        
    print(f"Successfully compiled {len(files_to_compile)} files into BOOT_CONTEXT.md")

if __name__ == "__main__":
    compile_boot_context()
