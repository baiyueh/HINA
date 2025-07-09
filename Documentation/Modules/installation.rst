Installation Steps
+++++++++

*HINA* is available on PyPI and can be installed using ``pip``, which will include the dependencies automatically:
To ensure running in a working environment please make sure the python version ``>=3.9``

.. code-block:: console

    pip install hina

For users who prefer installing dependencies manually, we provide a requirements.txt file on GitHub. To install HINA and its dependencies using this file:

.. code-block:: console
    
    git clone https://github.com/SHF-NAILResearchGroup/HINA.git
    cd HINA
    pip install -e .
    pip install -r requirements.txt

*HINA Dashboard APP* is available to build and run locally with Docker:

.. code-block:: console
    
    git clone https://github.com/SHF-NAILResearchGroup/HINA.git
    cd HINA
    docker compose up --build

Then, open the web browser and navigate to `http://localhost:8080` to access the *HINA Dashboard*.

**Source Code and Discussion Channel**

Available on Github, `SHF-NAILResearchGroup/HINA <https://github.com/SHF-NAILResearchGroup/HINA>`_.
Please report bugs, issues and feature extensions there. We also have `discussion channel <https://github.com/SHF-NAILResearchGroup/HINA/discussions>`_ available to discuss anything related to *HINA*:


**Testing and Continuous Integration**

*HINA* is equipped with automated testing on GitHub Actions to ensure that all functionalities work as expected. As part of CI/CD pipeline, this process helps maintain code quality and quickly catches any issues.

To run the tests manually, users need to clone the *HINA* GitHub repository.

1. **Clone the Repository**: First, clone the *HINA* GitHub repository to access the `Tests` folder.

   .. code-block:: console

       git clone https://github.com/SHF-NAILResearchGroup/HINA.git
       cd HINA

2. **Install the Required Packages**: Ensure all dependencies, including `pytest`, are installed by running the following commands:

   .. code-block:: console

       pip install -r requirements.txt
       pip install hina
       pip install httpx 
       pip install pytest
       hash -r  #Refresh shell's executable cache (needed if pytest was previously installed)
       

3. **Run the Tests**: Use `pytest` to execute all tests cases in the `HINA` folder.

   .. code-block:: console

       pytest hina/ 

4. **View the Results**: The output will display any failed tests and provide detailed information on each failed test case.

GitHub Actions runs these tests automatically with the latest stable versions of Python and relevant dependencies each time code is pushed to the repository or a pull request is made. For more information about workflows runs, see `Workflows <https://github.com/SHF-NAILResearchGroup/HINA/actions>`_ in the repository.
