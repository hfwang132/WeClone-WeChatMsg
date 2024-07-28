from llmtuner.data.formatter import FunctionFormatter, StringFormatter
from llmtuner.data.template import _register_template

default_prompt = "你叫茵茵，是用户的女朋友。用户的名字叫飞飞。请你模仿茵茵的语气与用户对话。"


def template_register():
    _register_template(
        name="chatglm3-weclone",
        default_system=(
            default_prompt
        ),
        format_user=StringFormatter(slots=[{"token": "<|user|>"}, "\n", "{{content}}", {"token": "<|assistant|>"}]),
        format_assistant=StringFormatter(slots=["\n", "{{content}}"]),
        format_system=StringFormatter(slots=[{"token": "[gMASK]"}, {"token": "sop"}, {"token": "<|system|>"}, "\n", "{{content}}"]),
        format_function=FunctionFormatter(slots=["{{name}}\n{{arguments}}"]),
        format_observation=StringFormatter(slots=[{"token": "<|observation|>"}, "\n", "{{content}}"]),
        stop_words=["<|user|>", "<|observation|>"],
        efficient_eos=True,
        force_system=True
    )
