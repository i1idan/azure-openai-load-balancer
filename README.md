# Azure OpenAI Load Balancer


## Usage

```python
# Example configuration

ENDPOINTS = '{
    "api_type": "azure",
    "base_url": "https://one.openai.azure.com/",
    "api_key_env": "key-one",
    "version": "version-one",
    "model_name": "model-one"
    "embedding_model": "embeddeing-one"

},
    {
    "api_type": "azure",
    "base_url": "https://two.openai.azure.com/",
    "api_key_env": "key-two",
    "version": "version-two",
    "model_name": "model-two"
    "embedding_model": "embeddeing-two"

}'
```



# How To Run

```bash
docker compose up -d
```