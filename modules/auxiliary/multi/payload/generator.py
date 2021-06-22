#!/usr/bin/env python3

#
# This module requires HatSploit: https://hatsploit.netlify.app
# Current source: https://github.com/EntySec/HatSploit
#

from hatsploit.module import Module


class HatSploitModule(Module):
    details = {
        'Name': "Multi Payload Generator",
        'Module': "auxiliary/multi/payload/generator",
        'Authors': [
            'Ivan Nikolsky (enty8080)'
        ],
        'Description': "Multi Payload Generator.",
        'Comments': [
            ''
        ],
        'Platform': "multi",
        'Risk': "high"
    }

    payload = {
        'Description': "Payload to use.",
        'Value': "linux/x64/shell_reverse_tcp",
        'Categories': None,
        'Architectures': None,
        'Platforms': None,
        'Types': None
    }

    options = {
        'LPATH': {
            'Description': "Local path.",
            'Value': "/tmp/payload.bin",
            'Type': None,
            'Required': True
        }
    }

    def run(self):
        local_file = self.parse_options(self.options)
        payload = self.payload['Payload']

        if payload:
            self.output_process(f"Saving to {local_file}...")
            with open(local_file, 'wb') as f:
                f.write(payload.encode() if isinstance(payload, str) else payload)
            self.output_success(f"Successfully saved to {local_file}!")
        else:
            self.output_error("Failed to generate payload!")
