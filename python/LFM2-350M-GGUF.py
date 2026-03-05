import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

# Load model and tokenizer
model_id = "LiquidAI/LFM2-350M"

model = AutoModelForCausalLM.from_pretrained(
    model_id,
    device_map="auto",
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    trust_remote_code=True,
)

tokenizer = AutoTokenizer.from_pretrained(model_id)

# Prompt
prompt = "What is C. elegans?"

# Apply chat template
inputs = tokenizer.apply_chat_template(
    [{"role": "user", "content": prompt}],
    add_generation_prompt=True,
    return_tensors="pt",
)

# Move inputs to model device
inputs = {k: v.to(model.device) for k, v in inputs.items()}

# Generate response
output = model.generate(
    **inputs,
    do_sample=True,
    temperature=0.3,
    repetition_penalty=1.05,
    max_new_tokens=512,
)

# Decode only the newly generated tokens
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(generated_text)