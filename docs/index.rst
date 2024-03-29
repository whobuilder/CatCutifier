Welcome to CatCutifier's documentation!
=====================

This document demonstrates the out-of-code documentation, which is perfect for the example-first documentation style.


Working with multi-file
=======================

A slightly confusing aspect of Sphinx is that for multi-file documentation to link to each section correctly, each file needs to be listed in the root table of contents.

This can be customized, which is a necessity for dynamic blog-style content, but it requires adjusting the sidebar code.

A typical place to put this root table of content is at the end of the index file, and it can also be hidden.

.. toctree::
   :maxdepth: 2

   self
   api/library_root

The above was generated using the following snippet. The `self` refers to this document, `api/library_root` refers to the autogenerated root file for API documentation from `exhale` as configured in `conf.py`.

.. code-block:: rst

   .. toctree::
      :maxdepth: 2

      self
      api/library_root